from django.core.management.base import BaseCommand
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from api.models import MLB_Player, MLB_Team, League

class Command(BaseCommand):
    help = 'Scraping MLB players to put them into the player table'

    def handle(self, *args, **kwargs):
        # Setup logging
        self.http = urllib3.PoolManager(maxsize=10)  # Increase maxsize to 10

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        #MLB_Player.objects.all().delete()
        years = range(2024, 2025)  # From 2000 to 2024
        teams = {
            
            "139": "TBR", "140": "TEX", "138": "STL", 
            
            "109": "ARI", "118": "KCR", "108": "LAA", "119": "LAD",
            "113": "CIN", "114": "CLE", "115": "COL", "116": "DET",
            "144": "ATL","141": "TOR", "120": "WSH", "136": "SEA",
            "134": "PIT", 
            "135": "SDP", "137": "SFG", "147": "NYY",
            "158": "MIL", "142": "MIN", "133": "OAK", "143": "PHI",
            "117": "HOU", 
            "110": "BAL", "121": "NYM", "146": "MIA", "117": "HOU",
            "111": "BOS", "112": "CHC", "145": "CWS"  
        }
        for year in years:
            for team_id, tid in teams.items():
                self.scrape_team_year(year, team_id, tid)

        logging.info("Scraping completed.")

    def scrape_team_year(self, year, team_id, tid):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        logging.info(f"Processing team {tid} for year {year}")
        driver.get("https://www.mlb.com/player/andrew-abbott-671096")
        time.sleep(2)

        if not self.retry_select_option(driver, "select[data-type='season']", str(year), retries=3):
            logging.error(f"Failed to select year {year} after retries")
            return

        if not self.retry_select_option(driver, "select[data-type='team']", team_id, retries=3):
            logging.error(f"Failed to select team {tid} after retries")
            return

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        player_elements = soup.select("select[data-type='player'] option")
        logging.info(f"Found {len(player_elements)} players for team {tid} in year {year}")

        for index, element in enumerate(player_elements):
            if index == 0:
                continue  # Skip the first element
            driver.get("https://www.mlb.com/player/andrew-abbott-671096")
            time.sleep(2)
            player_name = element.text.strip()
            player_id = element['value']
            player_slug = element.get('data-slug', player_id)
            link = f"https://www.mlb.com/player/{player_slug}"
            logging.info(f"Selected player: {player_name}")

            PID = player_id
            PYID = f"{PID}_{year}"

            try:
                team = MLB_Team.objects.get(TYID=f"{tid}_{year}")
                logging.info(f"Team with TYID '{tid}_{year}' found.")
            except MLB_Team.DoesNotExist:
                logging.error(f"Team with TYID '{tid}_{year}' not found.")
                continue

            try:
                league = League.objects.get(LYID=f"MLB_{year}")
                logging.info(f"League with LYID '{tid}_{year}' found.")
            except League.DoesNotExist:
                logging.error(f"League with LYID 'MLB_{year}' not found.")
                continue

            if not MLB_Player.objects.filter(PYID=PYID).exists():
                self.logger.info(f"Player: {player_name}, PID: {player_id}, PYID: {PYID}, TYID: {team}, LYID: {league}, year: {year}, link: {link}")
                
                batting_stats = self.scrape_player_stats(link, year, driver, 'hitting') or {}
                fielding_stats = self.scrape_player_stats(link, year, driver, 'fielding') or {}
                pitching_stats = self.scrape_player_stats(link, year, driver, 'pitching') or {}
                
                player = MLB_Player(
                    PID=player_id,
                    PYID=PYID,
                    TYID=team,
                    LYID=league,
                    player_name=player_name,
                    year=year,
                    link=link,
                    **batting_stats,
                    **fielding_stats,
                    **pitching_stats,
                )

                self.create_player(player)
            else:
                continue

    def retry_select_option(self, driver, selector, value, retries=3):
        for attempt in range(retries):
            try:
                select_element = Select(driver.find_element(By.CSS_SELECTOR, selector))
                select_element.select_by_value(value)
                time.sleep(2)
                return True
            except Exception as e:
                logging.error(f"Attempt {attempt + 1} - Error selecting {value}: {e}")
                if attempt == retries - 1:
                    return False

    def scrape_player_stats(self, link, year, driver, stat_type):
        driver.get(link)
        time.sleep(3)
        self.logger.info(f"Connected to link: {link}")
        try:
            self.handle_consent_banner(driver)
            self.logger.info(f"Trying to click stats button")
            stats_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "stats-nav-item"))
            )
            stats_button.click()
            time.sleep(2)
            self.logger.info(f"Clicked Stats button")

            section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "stats-block"))
            )
            stat_button = section.find_element(By.CSS_SELECTOR, f"button[data-type='{stat_type}']")
            stat_button.click()
            self.logger.info(f"{stat_type} button clicked")
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            career_table = soup.select_one("#careerTable tbody")
            if not career_table:
                self.logger.warning(f"No career table found for {link}")
                return {}

            stats_row = None
            for row in career_table.find_all("tr"):
                season = row.find("td", {"data-col": "0"}).text.strip()
                if season == str(year):
                    stats_row = row
                    break

            if not stats_row:
                self.logger.warning(f"No stats found for year {year} at {link}")
                return {}

            return self.extract_stats(stats_row, stat_type)
        except Exception:
            self.logger.error(f"No {stat_type} stats for: {link}")
            return {}

    def extract_stats(self, stats_row, stat_type):
        if stat_type == 'hitting':
            return {
                'at_bats': int(stats_row.find("td", {"data-col": "4"}).text.replace('\n', '').strip()),
                'runs': int(stats_row.find("td", {"data-col": "5"}).text.replace('\n', '').strip()),
                'hits': int(stats_row.find("td", {"data-col": "6"}).text.replace('\n', '').strip()),
                'total_bases': int(stats_row.find("td", {"data-col": "7"}).text.replace('\n', '').strip()),
                'doubles': int(stats_row.find("td", {"data-col": "8"}).text.replace('\n', '').strip()),
                'triples': int(stats_row.find("td", {"data-col": "9"}).text.replace('\n', '').strip()),
                'home_runs': int(stats_row.find("td", {"data-col": "10"}).text.replace('\n', '').strip()),
                'runs_batted_in': int(stats_row.find("td", {"data-col": "11"}).text.replace('\n', '').strip()),
                'walks': int(stats_row.find("td", {"data-col": "12"}).text.replace('\n', '').strip()),
                'strike_outs': int(stats_row.find("td", {"data-col": "13"}).text.replace('\n', '').strip()),
                'stolen_bases': int(stats_row.find("td", {"data-col": "14"}).text.replace('\n', '').strip()),
                'caught_stealing': int(stats_row.find("td", {"data-col": "15"}).text.replace('\n', '').strip()),
                'batting_average': float(stats_row.find("td", {"data-col": "17"}).text.replace('\n', '').strip()),
                'on_base_percentage': float(stats_row.find("td", {"data-col": "18"}).text.replace('\n', '').strip()),
                'slugging_percentage': float(stats_row.find("td", {"data-col": "19"}).text.replace('\n', '').strip()),
                'on_base_plus_slugging': float(stats_row.find("td", {"data-col": "20"}).text.replace('\n', '').strip()),
            }
        elif stat_type == 'fielding':
            return {
                'position': stats_row.find("td", {"data-col": "3"}).text.replace('\n', '').strip(),
                'games': int(stats_row.find("td", {"data-col": "4"}).text.replace('\n', '').strip()),
                'errors': int(stats_row.find("td", {"data-col": "10"}).text.replace('\n', '').strip()),
                'double_plays': int(stats_row.find("td", {"data-col": "11"}).text.replace('\n', '').strip()),
                'fielding_percentage': float(stats_row.find("td", {"data-col": "16"}).text.replace('\n', '').strip()),
            }
        elif stat_type == 'pitching':
            return {
                'wins': int(stats_row.find("td", {"data-col": "3"}).text.replace('\n', '').strip()),
                'losses': int(stats_row.find("td", {"data-col": "4"}).text.replace('\n', '').strip()),
                'earned_run_average': float(stats_row.find("td", {"data-col": "5"}).text.replace('\n', '').strip()),
                'p_games': int(stats_row.find("td", {"data-col": "6"}).text.replace('\n', '').strip()),
                'games_started': int(stats_row.find("td", {"data-col": "7"}).text.replace('\n', '').strip()),
                'complete_games': int(stats_row.find("td", {"data-col": "8"}).text.replace('\n', '').strip()),
                'shut_outs': int(stats_row.find("td", {"data-col": "9"}).text.replace('\n', '').strip()),
                'holds': int(stats_row.find("td", {"data-col": "10"}).text.replace('\n', '').strip()),
                'saves': int(stats_row.find("td", {"data-col": "11"}).text.replace('\n', '').strip()),
                'save_opportunities': int(stats_row.find("td", {"data-col": "12"}).text.replace('\n', '').strip()),
                'innings_pitched': float(stats_row.find("td", {"data-col": "13"}).text.replace('\n', '').strip()),
                'p_hits': int(stats_row.find("td", {"data-col": "14"}).text.replace('\n', '').strip()),
                'p_runs': int(stats_row.find("td", {"data-col": "15"}).text.replace('\n', '').strip()),
                'earned_runs': int(stats_row.find("td", {"data-col": "16"}).text.replace('\n', '').strip()),
                'p_home_runs': int(stats_row.find("td", {"data-col": "17"}).text.replace('\n', '').strip()),
                'number_of_pitches': int(stats_row.find("td", {"data-col": "18"}).text.replace('\n', '').strip()),
                'p_walks': int(stats_row.find("td", {"data-col": "20"}).text.replace('\n', '').strip()),
                'p_strike_outs': int(stats_row.find("td", {"data-col": "22"}).text.replace('\n', '').strip()),
                'batting_average_against': float(stats_row.find("td", {"data-col": "23"}).text.replace('\n', '').strip()),
                'whip': float(stats_row.find("td", {"data-col": "24"}).text.replace('\n', '').strip()),
            }

    def create_player(self, player):
        if not MLB_Player.objects.filter(PYID=player.PYID).exists():
            player.save()
            self.logger.info(f"Added player: {player.player_name} with PYID: {player.PYID}")
        else:
            self.logger.info(f"Player already exists: {player.player_name} with PYID: {player.PYID}")
            return

    def handle_consent_banner(self, driver):
        try:
            banner = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            banner.click()
        except Exception:
            self.logger.warning(f"Consent banner not found or not clickable")
