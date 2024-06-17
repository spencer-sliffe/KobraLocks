from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import json
from api.models import MLBGameLinks, MLBGameParlays
from concurrent.futures import ThreadPoolExecutor, as_completed

class Command(BaseCommand):
    help = 'Scrape MLB game parlays data from ESPNBet using stored game IDs'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        MLBGameParlays.objects.all().delete()
        self.logger.info("Cleared the MLBGameParlays table in the database.")
        # Fetch game IDs from the MLBGameLinks model
        game_links_obj = MLBGameLinks.objects.first()
        if not game_links_obj:
            self.logger.error("No game links found in the database.")
            return
        
        game_ids = game_links_obj.get_links()
        if not game_ids:
            self.logger.error("No game IDs found in the game links.")
            return

        self.logger.info(f"Fetched {len(game_ids)} game IDs from the database.")

        # Use ThreadPoolExecutor to scrape data concurrently
        with ThreadPoolExecutor(max_workers=20) as executor:  # Increased max_workers to 20
            futures = {executor.submit(self.scrape_game_page, game_id): game_id for game_id in game_ids}
            for future in as_completed(futures):
                game_id = futures[future]
                try:
                    future.result()
                    self.logger.info(f"Finished scraping game: {game_id}")
                except Exception as exc:
                    self.logger.error(f"Error scraping game {game_id}: {str(exc)}")

    def scrape_game_page(self, game_id):
        event_url = f"https://espnbet.com/sport/baseball/organization/united-states/competition/mlb/event/{game_id}"

        # Setup Selenium WebDriver once for all threads to minimize overhead
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(event_url)
        time.sleep(10)  # Reduced sleep time

        # Parse event page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
 
        sections = soup.find_all('details', class_='group overflow-hidden rounded bg-card-primary')
        self.logger.info(f"Found {len(sections)} parlay options on the page.")
        game = soup.find('div', class_="mb-10 mt-4 flex")
        teams = game.find_all('h2', class_='mt-2 text-[1.125rem] leading-[1.8125rem] text-primary')
        team1_text = teams[0].text.strip()
        team2_text = teams[1].text.strip()
        game_text = f"{team1_text} @ {team2_text}"
        for section in sections:
            self.logger.info("Processing MLB parlay section")
            self.handle_section(section, game_text, game_id)
        
        driver.quit()

    def handle_section(self, section, game_text, game_id):
        try:
            section_title = section.find('h2', class_='text-style-m-medium flex-1').text.strip()
            players_sections = section.find_all('div', class_='flex flex-col bg-card-primary')
            if len(players_sections) == 0:
                player_text = ''
                decimalodds = []
                americanodds = []
                for odd in section.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                    decimal_odd = odd.find('span', class_='font-medium text-selector-label-deselected')
                    decimal_odd_text = decimal_odd.text.strip() if decimal_odd else ""
                    decimalodds.append(decimal_odd_text)
                    american_odd = odd.find('span', class_='font-bold')
                    american_odd_text = american_odd.text.strip() if american_odd else ""
                    americanodds.append(american_odd_text)
                
                self.logger.info(f"Section: {section_title}, Player: {player_text}, Decimal Odds: {decimalodds}, American Odds: {americanodds}")

                MLBGameParlays.objects.create(
                    game_id=game_id,
                    game=game_text,
                    section_title=section_title,
                    player=player_text,
                    decimal_odds=json.dumps(decimalodds),
                    american_odds=json.dumps(americanodds)
                )
            else:
                for player in players_sections:
                    player_text = player.find('header', class_='text-style-s-medium text-primary text-left').text.strip()
                    decimalodds = []
                    americanodds = []
                    for odd in player.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                        decimal_odd = odd.find('span', class_='font-medium text-selector-label-deselected')
                        decimal_odd_text = decimal_odd.text.strip() if decimal_odd else ""
                        decimalodds.append(decimal_odd_text)
                        american_odd = odd.find('span', class_='font-bold')
                        american_odd_text = american_odd.text.strip() if american_odd else ""
                        americanodds.append(american_odd_text)
                
                # Check extracted values before saving
                    self.logger.info(f"Section: {section_title}, Player: {player_text}, Decimal Odds: {decimalodds}, American Odds: {americanodds}")
                
                    MLBGameParlays.objects.create(
                        game_id=game_id,
                        game=game_text,
                        section_title=section_title,
                        player=player_text,
                        decimal_odds=json.dumps(decimalodds),
                        american_odds=json.dumps(americanodds)
                    )
                    self.logger.info(f"Parlay Section saved: {section_title}")
        
        except Exception as e:
            self.logger.error(f"Error processing parlay section: {str(e)}")
