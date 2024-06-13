# backend/api/management/commands/scrape_nfl_player_totals.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import NFLPlayerTotals
import logging

class Command(BaseCommand):
    help = 'Scrape NFL player totals data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing NFL player total odds in the database
        NFLPlayerTotals.objects.all().delete()
        self.logger.info("Cleared the NFLPlayerTotals table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/football/organization/united-states/competition/nfl/section/player_totals"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        totals = soup.find_all('div', class_='flex p-0')

        self.logger.info(f"Found {len(totals)} totals on the page.")

        for total in totals:
            self.logger.info("Processing total odds")
            self.handle_totals(total)


        driver.quit()

    def handle_totals(self, total):
        try:
            title = total.find('div', class_='text-style-s-medium text-primary text-primary')
            row_title = title.text.strip()
            odds = total.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected')
            over_odds_1 = odds[0].find('span', class_='font-medium text-selector-label-deselected')
            text_over_odds_1 = over_odds_1.text.strip()
            over_odds_2 = odds[0].find('span', class_='font-bold')
            text_over_odds_2 = over_odds_2.text.strip()       
            under_odds_1 = odds[1].find('span', class_='font-medium text-selector-label-deselected')
            text_under_odds_1 = under_odds_1.text.strip()
            under_odds_2 = odds[1].find('span', class_='font-bold')
            text_under_odds_2 = under_odds_2.text.strip()
            NFLPlayerTotals.objects.create(
                row_title=row_title,
                over_decimal_odds=text_over_odds_1,
                under_decimal_odds=text_over_odds_2,
                over_american_odds=text_under_odds_1,
                under_american_odds=text_under_odds_2
            )

            self.logger.info(f"Odds for {row_title} saved")
        except Exception as e:
            self.logger.error(f"Error processing playoff odds: {str(e)}")
