# backend/api/management/commands/scrape_nfl_division_specials.py
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import NFLDivisionSpecials
import logging
import json

class Command(BaseCommand):
    help = 'Scrape NFL specials data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing NFL Specials in the database
        NFLDivisionSpecials.objects.all().delete()
        self.logger.info("Cleared the NFLSpecials table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/football/organization/united-states/competition/nfl/section/division-specials"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

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
            allbettitles = []
            allodds = []
            allteams = []
            for allteam in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                team = allteam.find('span', class_='font-medium text-selector-label-deselected')
                team_text = team.text.strip()
                allteams.append(team_text)
            for allbettitle in special.find_all('button', class_='flex w-full items-center justify-between pr-4 pt-2 text-left cursor-default'):
                bet = allbettitle.find('div', class_='text-style-s-medium text-primary text-primary')
                bet_title = bet.text.strip()
                allbettitles.append(bet_title)
            for allodd in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                odd_detail = allodd.find('span', class_='font-bold')
                odd = odd_detail.text.strip()
                allodds.append(odd)

            # Create MLBFutures entry
            NFLDivisionSpecials.objects.create(
                section_title=section_title,
                bet_titles=json.dumps(allbettitles),  # Encode list as JSON string
                team_titles=json.dumps(allteams),   # Encode list as JSON string
                odds=json.dumps(allodds)    # Encode list as JSON string
            )
            self.logger.info(f"Special saved: {section_title}")
        except Exception as e:
            self.logger.error(f"Error processing special: {str(e)}")
