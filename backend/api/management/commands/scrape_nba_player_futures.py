# backend/api/management/commands/scrape_nba_player_futures.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import NBAPlayerFutures
import logging
import json

class Command(BaseCommand):
    help = 'Scrape NBA player futures data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing MLB games in the database
        NBAPlayerFutures.objects.all().delete()
        self.logger.info("Cleared the NBAFutures table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/basketball/organization/united-states/competition/nba/section/player_futures"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        futures = soup.find_all('details', class_='group overflow-hidden rounded bg-card-primary')

        self.logger.info(f"Found {len(futures)} player futures on the page.")

        for future in futures:
            self.logger.info("Processing player Future")
            self.handle_future(future)

        driver.quit()

    def handle_future(self, future):
        try:
            section = future.find('h2', class_='text-style-m-medium flex-1')
            section_title = section.text.strip()
            allplayers = []
            allodds = []
            for allplayer in future.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                player_detail = allplayer.find('span', class_='font-medium text-selector-label-deselected')
                player = player_detail.text.strip()
                allplayers.append(player)
            for allodd in future.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                odd_detail = allodd.find('span', class_='font-bold')
                odd = odd_detail.text.strip()
                allodds.append(odd)

            # Create MLBFutures entry
            NBAPlayerFutures.objects.create(
                section_title=section_title,
                players=json.dumps(allplayers),  # Encode list as JSON string
                odds=json.dumps(allodds)    # Encode list as JSON string
            )
            self.logger.info(f"Player Future saved: {section_title}")
        except Exception as e:
            self.logger.error(f"Error processing player future: {str(e)}")
