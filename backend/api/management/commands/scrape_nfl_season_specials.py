# backend/api/management/commands/scrape_nfl_season_specials.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import NFLSeasonSpecials
import logging
import json

class Command(BaseCommand):
    help = 'Scrape NFL specials data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing NFL Season Specials in the database
        NFLSeasonSpecials.objects.all().delete()
        self.logger.info("Cleared the NFL Season Special table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/football/organization/united-states/competition/nfl/section/season_specials"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        specials = soup.find_all('details', class_='group overflow-hidden rounded bg-card-primary')

        self.logger.info(f"Found {len(specials)} specials on the page.")

        for special in specials:
            self.logger.info("Processing Special")
            self.handle_special(special)

        driver.quit()

    def handle_special(self, special):
        try:
            section = special.find('h2', class_='text-style-m-medium flex-1')
            section_title = section.text.strip()
            allteams = []
            allodds = []
            for allteam in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                team_detail = allteam.find('span', class_='font-medium text-selector-label-deselected')
                team = team_detail.text.strip()
                allteams.append(team)
            for allodd in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                odd_detail = allodd.find('span', class_='font-bold')
                odd = odd_detail.text.strip()
                allodds.append(odd)

            # Create NFLSpecials entry
            NFLSeasonSpecials.objects.create(
                section_title=section_title,
                teams=json.dumps(allteams),  # Encode list as JSON string
                odds=json.dumps(allodds)    # Encode list as JSON string
            )
            self.logger.info(f"Special saved: {section_title}")
        except Exception as e:
            self.logger.error(f"Error processing special: {str(e)}")
