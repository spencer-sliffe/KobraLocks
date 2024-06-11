# backend/api/management/commands/scrape_mls_games.py
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import MLSGame
import datetime
import pytz
import logging

class Command(BaseCommand):
    help = 'Scrape MLS games data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing MLS games in the database
        MLSGame.objects.all().delete()
        self.logger.info("Cleared the MLSGame table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/soccer/organization/usa/competition/mls"
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        games = soup.find_all('article', class_='b-default pt-2 first:pt-0 last:pb-0 first:pt-0')

        self.logger.info(f"Found {len(games)} games on the page.")

        for game in games:
            live_indicator = game.find('div', class_='text-style-2xs-medium text-live inline-flex items-center gap-x-1')
            if live_indicator and 'LIVE' in live_indicator.text:
                self.logger.info("Processing live game")
                self.handle_live_game(game)
            else:
                self.logger.info("Processing scheduled game")
                self.handle_scheduled_game(game)

        driver.quit()

    def handle_live_game(self, game):
        try:
            teams = game.find_all('div', class_='text-style-s-medium text-primary text-primary')
            if len(teams) < 2:
                self.logger.error("Not enough teams information found for the live game.")
                return
            
            team1_name = teams[0].text.strip()
            team2_name = teams[1].text.strip()
            scores = game.find_all('div', class_='text-style-m-medium flex text-right align-middle')
            team1_score = int(scores[0].text.strip()) if len(scores) > 0 else None
            team2_score = int(scores[1].text.strip()) if len(scores) > 1 else None

            clock = game.find('span', class_='flex items-center gap-1 py-0.5').text.strip()

            odds_buttons = game.find_all('button', class_='button-bet-selector-hidden') + game.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected')
            if len(odds_buttons) >= 3:
                team1_odds = odds_buttons[0].find('span', {'class': 'font-bold'}).text.strip()
                draw_odds = odds_buttons[1].find('span', {'class': 'font-bold'}).text.strip()
                team2_odds = odds_buttons[2].find('span', {'class': 'font-bold'}).text.strip()

                MLSGame.objects.create(
                    team1=team1_name,
                    team2=team2_name,
                    live=True,
                    clock=clock,
                    team1_score=team1_score,
                    team2_score=team2_score,
                    team1_odds=team1_odds,
                    draw_odds=draw_odds,
                    team2_odds= team2_odds,
                )
                self.logger.info(f"Live game saved: {team1_name} vs {team2_name}")
            else:
                self.logger.error("Not enough odds information found for the live game.")
        except Exception as e:
            self.logger.error(f"Error processing live game: {str(e)}")

    def handle_scheduled_game(self, game):
        try:
            time_info_button = game.find('button', class_='text-primary flex-wrap items-center gap-x-2 text-left flex pr-4 w-[47%]')
            if not time_info_button:
                self.logger.error("Unable to find time info button for the scheduled game.")
                return

            game_time = time_info_button.find('span').text.strip()

            #time_info_parts = time_info_button.text.strip().split('·')
            #if len(time_info_parts) < 2:
            #    self.logger.error("Time info format incorrect.")
            #    return

            #time_info = time_info_parts[1].strip()
            #game_time = datetime.datetime.strptime(time_info, '%I:%M %p')

            # Make the datetime object timezone-aware
            #game_time = pytz.timezone('UTC').localize(game_time)

            teams = game.find_all('div', class_='text-style-s-medium text-primary mr-1 text-primary')
            if len(teams) < 2:
                self.logger.error("Not enough teams information found for the scheduled game.")
                return

            team1_name = teams[0].text.strip()
            team2_name = teams[1].text.strip()

            team_records = game.find_all('div', class_='text-style-2xs-medium text-subdued-primary mt-0.5')
            team1_record = team_records[0].text.strip()
            team2_record = team_records[1].text.strip()


            odds_buttons = game.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected')
            if len(odds_buttons) >= 3:
                team1_odds = odds_buttons[0].find('span', {'class': 'font-bold'}).text.strip()
                draw_odds = odds_buttons[1].find('span', {'class': 'font-bold'}).text.strip()
                team2_odds = odds_buttons[2].find('span', {'class': 'font-bold'}).text.strip()

                MLSGame.objects.create(
                    team1=team1_name,
                    team2=team2_name,
                    team1_record=team1_record,
                    team2_record=team2_record,
                    game_time=game_time,
                    live=False,
                    team1_odds=team1_odds,
                    draw_odds=draw_odds,
                    team2_odds=team2_odds,
                )
                self.logger.info(f"Scheduled game saved: {team1_name} vs {team2_name}")
            else:
                self.logger.error("Not enough odds information found for the scheduled game.")
        except Exception as e:
            self.logger.error(f"Error processing scheduled game: {str(e)}")
