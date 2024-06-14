# backend/api/management/commands/scrape_mlb_games.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import MLBGame
import logging

class Command(BaseCommand):
    help = 'Scrape MLB games data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing MLB games in the database
        MLBGame.objects.all().delete()
        self.logger.info("Cleared the MLBGame table in the database.")

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/baseball/organization/united-states/competition/mlb"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

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

            inning_info = game.find('span', class_='flex items-center gap-1 py-0.5').text.strip()
            inning_state = inning_info  # Store the combined inning state

            balls, strikes, outs = 0, 0, 0
            for part in inning_info.split():
                if 'B:' in part:
                    balls = int(part.split(':')[1])
                elif 'S:' in part:
                    strikes = int(part.split(':')[1])
                elif 'O:' in part:
                    outs = int(part.split(':')[1])

            odds_buttons = game.find_all('button', class_='button-bet-selector-hidden') + game.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected')
            team1_spread = odds_buttons[0].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 0 else None
            team1_spread_odds = odds_buttons[0].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 0 else None
            team1_total = odds_buttons[1].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 1 else None
            team1_total_odds = odds_buttons[1].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 1 else None
            team1_money = odds_buttons[2].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 2 else None

            team2_spread = odds_buttons[3].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 3 else None
            team2_spread_odds = odds_buttons[3].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 3 else None
            team2_total = odds_buttons[4].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 4 else None
            team2_total_odds = odds_buttons[4].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 4 else None
            team2_money = odds_buttons[5].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 5 else None

            MLBGame.objects.create(
                team1=team1_name,
                team2=team2_name,
                live=True,
                inning_state=inning_state,
                team1_score=team1_score,
                team2_score=team2_score,
                balls=balls,
                strikes=strikes,
                outs=outs,
                team1_spread=f"{team1_spread} {team1_spread_odds}",
                team1_total=f"{team1_total} {team1_total_odds}",
                team1_money=team1_money,
                team2_spread=f"{team2_spread} {team2_spread_odds}",
                team2_total=f"{team2_total} {team2_total_odds}",
                team2_money=team2_money
            )
            self.logger.info(f"Live game saved: {team1_name} vs {team2_name}")
        except Exception as e:
            self.logger.error(f"Error processing live game: {str(e)}")

    def handle_scheduled_game(self, game):
        try:
            time_info_button = game.find('button', class_='text-primary flex-wrap items-center gap-x-2 text-left flex pr-4 w-[47%]')
            if not time_info_button:
                self.logger.error("Unable to find time info button for the scheduled game.")
                return

            #time_info = time_info_button.text.strip().split('·')[1].strip()
            game_time = time_info_button.find('span').text.strip()
            # Make the datetime object timezone-aware
            #game_time = pytz.timezone('UTC').localize(game_time)

            teams = game.find_all('div', class_='text-style-s-medium text-primary text-primary')
            team1_name = teams[0].text.strip()
            team2_name = teams[1].text.strip()

            odds_buttons = game.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected')
            team1_spread = odds_buttons[0].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 0 else None
            team1_spread_odds = odds_buttons[0].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 0 else None
            team1_total = odds_buttons[1].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 1 else None
            team1_total_odds = odds_buttons[1].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 1 else None
            team1_money = odds_buttons[2].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 2 else None

            team2_spread = odds_buttons[3].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 3 else None
            team2_spread_odds = odds_buttons[3].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 3 else None
            team2_total = odds_buttons[4].find('span', {'class': 'font-medium text-selector-label-deselected'}).text.strip() if len(odds_buttons) > 4 else None
            team2_total_odds = odds_buttons[4].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 4 else None
            team2_money = odds_buttons[5].find('span', {'class': 'font-bold'}).text.strip() if len(odds_buttons) > 5 else None

            MLBGame.objects.create(
                team1=team1_name,
                team2=team2_name,
                game_time=game_time,
                live=False,
                team1_spread=f"{team1_spread} {team1_spread_odds}",
                team1_total=f"{team1_total} {team1_total_odds}",
                team1_money=team1_money,
                team2_spread=f"{team2_spread} {team2_spread_odds}",
                team2_total=f"{team2_total} {team2_total_odds}",
                team2_money=team2_money
            )
            self.logger.info(f"Scheduled game saved: {team1_name} vs {team2_name}")
        except Exception as e:
            self.logger.error(f"Error processing scheduled game: {str(e)}")
