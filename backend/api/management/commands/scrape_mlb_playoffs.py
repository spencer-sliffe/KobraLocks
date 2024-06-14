# backend/api/management/commands/scrape_mlb_playoffs.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import MLBTeamPlayoffs
import logging

class Command(BaseCommand):
    help = 'Scrape MLB games data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing MLB playoff odds in the database
        MLBTeamPlayoffs.objects.all().delete()
        self.logger.info("Cleared the MLBGame table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/baseball/organization/united-states/competition/mlb/section/to-make-the-playoffs"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        playoffs = soup.find_all('div', class_='flex p-0')

        self.logger.info(f"Found {len(playoffs)} playoffs on the page.")

        for playoff in playoffs:
            self.logger.info("Processing playoff odds")
            self.handle_playoff(playoff)


        driver.quit()

    def handle_playoff(self, playoff):
        try:
            title = playoff.find('div', class_='text-style-s-medium text-primary text-primary')
            row_title = title.text.strip()
            odds = playoff.find_all('span', class_='font-bold')
            yes_odds = odds[0].text.strip()
            no_odds = odds[1].text.strip()


            MLBTeamPlayoffs.objects.create(
                row_title=row_title,
                yes_odds=yes_odds,
                no_odds=no_odds
            )
            self.logger.info(f"Playoff for {row_title} saved")
        except Exception as e:
            self.logger.error(f"Error processing playoff odds: {str(e)}")
