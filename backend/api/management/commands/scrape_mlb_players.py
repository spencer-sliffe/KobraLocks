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
        MLB_Player.objects.all().delete()
        years = range(2020, 2025)  # From 2000 to 2024
        teams = {
            "109": "ARI", "144": "ATL", "110": "BAL",
            "111": "BOS", "112": "CHC", "145": "CWS",
            "113": "CIN", "114": "CLE", "115": "COL", "116": "DET",
            "117": "HOU", "118": "KCR", "108": "LAA", "119": "LAD",
            "146": "MIA", "158": "MIL", "142": "MIN", "121": "NYM",
            "147": "NYY", "133": "OAK", "143": "PHI",
            "134": "PIT", "135": "SDP", "137": "SFG", 
            "141": "TOR", "120": "WSH", "136": "SEA",
            "138": "STL", "139": "TBR", "140": "TEX"

        }
        for team_id, tid in teams.items():
            for year in years:
                self.scrape_team_year(year, team_id, tid)

        logging.info("Scraping completed.")

    def scrape_team_year(self, year, team_id, tid):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        try:
            logging.info(f"Processing team {tid} for year {year}")
            driver.get("https://www.mlb.com/player/andrew-abbott-671096")
            time.sleep(2)
            retries = 3
            for attempt in range(retries):
                try:
                    # Select the year
                    year_select = Select(driver.find_element(By.CSS_SELECTOR, "select[data-type='season']"))
                    year_select.select_by_value(str(year))
                    time.sleep(2)
                    break
                except Exception as e:
                    logging.error(f"Attempt {attempt + 1} - Error selecting year {year}: {e}")
                    if attempt == retries - 1:
                        raise

            for attempt in range(retries):
                try:
                    # Select the team
                    team_select = Select(driver.find_element(By.CSS_SELECTOR, "select[data-type='team']"))
                    team_select.select_by_value(team_id)
                    time.sleep(2)
                    break
                except Exception as e:
                    logging.error(f"Attempt {attempt + 1} - Error selecting team {tid}: {e}")
                    if attempt == retries - 1:
                        raise

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
                    
                    batting_stats = self.scrape_player_batting_stats(link, year, driver)
                    fielding_stats = self.scrape_player_fielding_stats(link, year, driver)
                    pitching_stats = self.scrape_player_pitching_stats(link, year, driver)

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
        except Exception as e:
            logging.error(f"Error processing team {tid} for year {year}: {e}")
        finally:
            driver.quit()

        # Use ThreadPoolExecutor to run the function concurrently
        

    def scrape_player_batting_stats(self, link, year, driver):
        driver.get(link)
        time.sleep(3)
        self.logger.info(f"Connected to link: {link}")
        try:
            self.handle_consent_banner(driver)
            self.logger.info(f"Trying to click stats button")
            stats_button = driver.find_element(By.ID, "stats-nav-item")
            stats_button.click()
            time.sleep(2)
            self.logger.info(f"Clicked Stats button")
            self.logger.info(f"trying to click batting button")
            section = driver.find_element(By.ID, "stats-block")
            batting_button = section.find_element(By.CSS_SELECTOR, "button[data-type='hitting']")
            batting_button.click()
            self.logger.info(f"batting button clicked")
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

            stats = {
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
            return stats
        except Exception:
            self.logger.error(f"No Batting stats for: {link}")
            return{}

    def scrape_player_fielding_stats(self, link, year, driver):
        driver.get(link)
        time.sleep(3)
        self.logger.info(f"Connected to link: {link}") 
        try:
            self.handle_consent_banner(driver)
            self.logger.info(f"Trying to click stats button")
            stats_button = driver.find_element(By.ID, "stats-nav-item")
            stats_button.click()
            time.sleep(2)
            self.logger.info(f"Clicked Stats button")
            self.logger.info(f"trying to click fielding button")
            section = driver.find_element(By.ID, "stats-block")       
            fielding_button = section.find_element(By.CSS_SELECTOR, "button[data-type='fielding']")
            fielding_button.click()
            self.logger.info(f"fielding button clicked")
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


            stats = {
                'position': stats_row.find("td", {"data-col": "3"}).text.replace('\n', '').strip(),
                'games': int(stats_row.find("td", {"data-col": "4"}).text.replace('\n', '').strip()),
                'errors': int(stats_row.find("td", {"data-col": "10"}).text.replace('\n', '').strip()),
                'double_plays': int(stats_row.find("td", {"data-col": "11"}).text.replace('\n', '').strip()),
                'fielding_percentage': float(stats_row.find("td", {"data-col": "16"}).text.replace('\n', '').strip()),
            }
            return stats
        except Exception:
            self.logger.error(f"No Fielding stats for: {link}")
            return{}

    def scrape_player_pitching_stats(self, link, year, driver):
        driver.get(link)
        time.sleep(3)
        self.logger.info(f"Connected to link: {link}")
        try:  
            self.handle_consent_banner(driver)
            self.logger.info(f"Trying to click stats button")
            stats_button = driver.find_element(By.ID, "stats-nav-item")
            stats_button.click()
            time.sleep(2)
            self.logger.info(f"Clicked Stats button")
            self.logger.info(f"trying to click pitching button")
            section = driver.find_element(By.ID, "stats-block")
            pitching_button = section.find_element(By.CSS_SELECTOR, "button[data-type='pitching']")
            if not pitching_button:
                self.logger.warning(f"No pitching stats available for {link}")
                return {}
            pitching_button.click()
            self.logger.info(f"pitching button clicked")
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


            stats = {
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
            return stats
        except Exception:
            self.logger.error(f"No Pitching stats for: {link}")
            return{}

    def create_player(self, player):
        if not MLB_Player.objects.filter(PYID=player.PYID).exists():
            player.save()
            self.logger.info(f"Added player: {player.player_name} with PYID: {player.PYID}")
        else:
            self.logger.info(f"Player already exists: {player.player_name} with PYID: {player.PYID}")


    def handle_consent_banner(self, driver):
        try:
            if driver.find_element(By.ID, "onetrust-accept-btn-handler"):
                banner = driver.find_element(By.ID, "onetrust-accept-btn-handler")
                banner.click()
        except Exception:
            self.logger.warning(f"Consent banner not found or not clickable")
