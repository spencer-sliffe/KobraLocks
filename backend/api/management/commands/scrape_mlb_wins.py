# backend/api/management/commands/scrape_mlb_wins.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import MLBWinTotals
import logging

class Command(BaseCommand):
    help = 'Scrape MLB team win odds data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing MLB playoff odds in the database
        MLBWinTotals.objects.all().delete()
        self.logger.info("Cleared the MLB win odds table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/baseball/organization/united-states/competition/mlb/section/win-totals"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        wins = soup.find_all('details', class_='group overflow-hidden rounded bg-card-primary')

        self.logger.info(f"Found {len(wins)} teams on the page.")

        for win in wins:
            self.logger.info("Processing teams win odds")
            self.handle_wins(win)


        driver.quit()

    def handle_wins(self, win):
        try:
            team_title = win.find('h2', class_='text-style-m-medium flex-1')
            team = team_title.text.strip()
            titles = win.find_all('div', class_='text-style-s-medium text-primary text-primary')
            over_title = titles[0].text.strip()
            under_title = titles[1].text.strip()
            
            odds = win.find_all('span', class_='font-bold')
            over_odds = odds[0].text.strip()
            under_odds = odds[1].text.strip()


            MLBWinTotals.objects.create(
                team=team,
                over_title=over_title,
                under_title=under_title,
                over_odds=over_odds,
                under_odds=under_odds
            )
            self.logger.info(f"Win odds for {team} saved")
        except Exception as e:
            self.logger.error(f"Error processing win odds: {str(e)}")