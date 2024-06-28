from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import random
from concurrent.futures import ThreadPoolExecutor
from api.models import NFL_player_link, NFL_Player, NFL_Team, NFL_Division, League

class Command(BaseCommand):
    help = 'Scraping NFL players to put them into the player table'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        NFL_Player.objects.all().delete()

        with ThreadPoolExecutor(max_workers=5) as executor:
            player_links = NFL_player_link.objects.all()
            futures = [executor.submit(self.scrape_player, link_obj.link, options) for link_obj in player_links]
            
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    self.logger.error(f"Error scraping player: {e}")

    def scrape_player(self, link, options):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        try:
            self.logger.info(f"Connecting to link {link}")
            driver.get(link)
            time.sleep(3)  # Wait for the page to load
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            player_link = soup.find('div', class_='PageLayout__Main')
            header_link = soup.find('div', class_='PlayerHeader__Main flex items-center')

            if player_link and header_link:
                self.logger.info(f"Handling player")
                self.handle_player(player_link, header_link, link)
            else:
                self.logger.error(f"Error finding player or header link for URL: {link}")
        finally:
            driver.quit()

    def handle_player(self, player_link, header_link, link):
        teams = {
            "BUF": "AFC_East", "MIA": "AFC_East", "NE": "AFC_East", "NYJ": "AFC_East",
            "BAL": "AFC_North", "CIN": "AFC_North", "CLE": "AFC_North", "PIT": "AFC_North",
            "HOU": "AFC_South", "IND": "AFC_South", "JAX": "AFC_South", "TEN": "AFC_South",
            "DEN": "AFC_West", "KC": "AFC_West", "LV": "AFC_West", "LAC": "AFC_West",
            "DAL": "NFC_East", "NYG": "NFC_East", "PHI": "NFC_East", "WAS": "NFC_East",
            "CHI": "NFC_North", "DET": "NFC_North", "GB": "NFC_North", "MIN": "NFC_North",
            "ATL": "NFC_South", "CAR": "NFC_South", "NO": "NFC_South", "TB": "NFC_South",
            "ARI": "NFC_West", "LAR": "NFC_West", "SF": "NFC_West", "SEA": "NFC_West"
        }

        positions = {
            "Quarterback": "QB", "Running Back": "RB", "Wide Receiver": "WR", "Tight End": "TE", "Kicker": "K"
        }
        
        stat_table_names = {'Passing', 'Rushing', 'Receiving', 'Kicking'}

        try:
            # player_name
            name_section = header_link.find('h1', class_='PlayerHeader__Name flex flex-column ttu fw-bold pr4 h3')
            if not name_section:
                self.logger.error(f"Name section not found in header link for URL: {link}")
                return
                
            first_name = name_section.find('span', class_='truncate min-w-0 fw-light')
            last_name = name_section.find('span', class_='truncate min-w-0')
            if not first_name or not last_name:
                self.logger.error(f"First name or last name not found in name section for URL: {link}")
                return
                
            first_name = first_name.text.strip()
            last_name = last_name.text.strip()
            player_name = f"{last_name}, {first_name}"
            self.logger.info(f"Handled player name: {player_name}")

            # position
            position_section = header_link.find('ul', class_='PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap')
            if not position_section:
                self.logger.error(f"Position section not found in header link for URL: {link}")
                return
                
            position_name_section = position_section.find_all('li')
            if len(position_name_section) < 3:
                self.logger.error(f"Position name section not found or incomplete in header link for URL: {link}")
                return
                
            position = position_name_section[2].text.strip()
            self.logger.info(f"Handled player position: {position}")

            # years
            years = self.get_player_years(player_link, stat_table_names)
            self.logger.info(f"Handled player years: {years}")

            # player id
            pid = self.generate_unique_id()
            self.logger.info(f"Handled player pid: {pid}")

            # stats
            self.logger.info(f"Handling stats")
            for year in years:
                lyid = f"NFL_{year}"
                team = self.get_player_team(year, player_link, stat_table_names)
                if not team:
                    self.logger.error(f"Team not found for year {year} in URL: {link}")
                    continue
                tyid = f"{team}_{year}"
                did = teams.get(team)
                dyid = f"{did}_{year}"
                
                # Fetch the actual instances
                nfl_team = NFL_Team.objects.get(TYID=tyid)
                nfl_division = NFL_Division.objects.get(DYID=dyid)
                league = League.objects.get(LYID=lyid)
                
                pyid = f"{pid}_{year}"
                stats = self.handle_stats(player_name, position, pid, pyid, nfl_division, nfl_team, league, player_link, year, link, stat_table_names)
                if stats:
                    player_data = stats  # use stats dictionary directly
                    self.create_player(player_data)
                else:
                    self.logger.info(f"No stats found for player {player_name} for year {year} in URL: {link}")
                
        except AttributeError as e:
            self.logger.error(f"Error processing player: {e}")

    def get_player_years(self, player, stat_table_names):
        years = []
        tables = player.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left pt4')
        for table in tables:
            table_title = table.find('div', class_='Table__Title').text.strip()
            self.logger.info(f"table title: {table_title}")
            if table_title in stat_table_names:
                year_section = table.find('tbody', class_='Table__TBODY')
                if not year_section:
                    self.logger.error(f"Year section not found in table with title {table_title}")
                    continue
                year_rows = year_section.find_all('tr', class_='Table__TR Table__TR--sm Table__even')
                for year_row in year_rows:
                    value_columns = year_row.find_all('td', class_='Table__TD')
                    if len(value_columns) > 1:
                        value = value_columns[0].text.strip()
                        if value not in years and value != "Career":
                            years.append(value)
        self.logger.info(f"Found years: {years}")
        return years

    def get_player_team(self, year, player, stat_table_names):
        tables = player.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left pt4')
        for table in tables:
            table_title = table.find('div', class_='Table__Title').text.strip()
            if table_title in stat_table_names:
                year_section = table.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left')
                if not year_section:
                    self.logger.error(f"Year section not found in table with title {table_title}")
                    continue
                year_rows = year_section.find_all('tr', class_='Table__TR Table__TR--sm Table__even')
                for year_row in year_rows:
                    value_columns = year_row.find_all('td', class_='Table__TD')
                    if len(value_columns) > 1:
                        value = value_columns[0].text.strip()
                        self.logger.info(f"player team year: {value}")
                        if value == year:
                            team = value_columns[1].find('a', class_='AnchorLink pl2').text.strip()
                            if team:
                                self.logger.info(f"player team: {team}")
                                return team
        self.logger.error(f"No team found for year {year}")
        return None

    def handle_stats(self, player_name, position, pid, pyid, dyid, tyid, lyid, player_link, year, link, stat_table_names):
        stats = {}
        tables = player_link.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left pt4')
        for table in tables:
            table_title = table.find('div', class_='Table__Title').text.strip()
            if table_title in stat_table_names:
                if table_title == 'Passing':
                    passing_stats = self.extract_stats(table_title, table, year)
                    if not passing_stats:
                        self.logger.info(f"No passing stats for player {player_name} for year {year}")
                        continue
                    stats.update(passing_stats)
                    self.logger.info(f"Finished extracting passing stats for year {year}")
                elif table_title == 'Rushing':
                    rushing_stats = self.extract_stats(table_title, table, year)
                    if not rushing_stats:
                        self.logger.info(f"No rushing stats for player {player_name} for year {year}")
                        continue
                    stats.update(rushing_stats)
                    self.logger.info(f"Finished extracting rushing stats for year {year}")
                elif table_title == 'Receiving':
                    receiving_stats = self.extract_stats(table_title, table, year)
                    if not receiving_stats:
                        self.logger.info(f"No receiving stats for player {player_name} for year {year}")
                        continue
                    stats.update(receiving_stats)
                    self.logger.info(f"Finished extracting receiving stats for year {year}")
                elif table_title == 'Kicking':
                    kicking_stats = self.extract_stats(table_title, table, year)
                    if not kicking_stats:
                        self.logger.info(f"No kicking stats for player {player_name} for year {year}")
                        continue
                    stats.update(kicking_stats)
                    self.logger.info(f"Finished extracting kicking stats for year {year}")

        stats.update({
            'PID': pid,
            'PYID': pyid,
            'TYID': tyid,
            'DYID': dyid,
            'LYID': lyid,
            'player_name': player_name,
            'year': year,
            'link': link,
            'position': position
        })
        
        return stats
    
    def extract_stats(self, table_title, table, year):
        index = 0
        stats = {}
        year_section = table.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left')
        if not year_section:
            self.logger.error(f"Year section not found in table with title {table_title}")
            return stats
        year_row_section = year_section.find('tbody', class_='Table__TBODY')
        year_rows = year_row_section.find_all('tr', class_='Table__TR Table__TR--sm Table__even')
        for year_row in year_rows:
            value_columns = year_row.find_all('td', class_='Table__TD')
            if len(value_columns) > 1:
                value = value_columns[0].text.strip()
                if value != year:
                    index += 1
                else:
                    self.logger.info(f"index: {index}")
                    break
        
        table_stat_section = table.find('div', class_='Table__ScrollerWrapper relative overflow-hidden')
        if not table_stat_section:
            self.logger.error(f"Table stat section not found in table with title {table_title}")
            return stats
        table_stats = table_stat_section.find('tbody', class_='Table__TBODY')
        stat_rows = table_stats.find_all('tr', class_='Table__TR Table__TR--sm Table__even')

        if index >= len(stat_rows):
            self.logger.error(f"Index {index} out of range for stat_rows with length {len(stat_rows)} in table with title {table_title}")
            return stats

        stat_row = stat_rows[index]
        stat_columns = stat_row.find_all('td', class_='Table__TD')
        self.logger.info(f"Extracting stats for table title: {table_title}, year: {year}")

        for i, col in enumerate(stat_columns):
            if col is None:
                self.logger.error(f"Column {i} is None in table with title {table_title} for year {year}")
                return stats
            else:
                self.logger.info(f"Column {i}: {col.text.strip()}")

        if table_title == 'Passing':
            stats = {
                'games_played': int(stat_columns[0].text.strip().replace(',', '')),
                'pass_attempts': int(stat_columns[2].text.strip().replace(',', '')),
                'pass_completions': int(stat_columns[1].text.strip().replace(',', '')),
                'completion_percentage': float(stat_columns[3].text.strip().replace(',', '')),
                'passing_yards': int(stat_columns[4].text.strip().replace(',', '')),
                'yards_per_attempt': float(stat_columns[5].text.strip().replace(',', '')),
                'passing_touchdowns': int(stat_columns[6].text.strip().replace(',', '')),
                'interceptions': int(stat_columns[7].text.strip().replace(',', '')),
                'sacks': int(stat_columns[9].text.strip().replace(',', '')),
                'QB_rating': float(stat_columns[10].text.strip().replace(',', ''))
            }
        elif table_title == 'Rushing':
            stats = {
                'rushing_attempts': int(stat_columns[1].text.strip().replace(',', '')),
                'rushing_yards': int(stat_columns[2].text.strip().replace(',', '')),
                'rushing_average': float(stat_columns[3].text.strip().replace(',', '')),
                'rushing_touchdowns': int(stat_columns[4].text.strip().replace(',', '')),
                'rushing_first_downs': int(stat_columns[6].text.strip().replace(',', '')),
                'fumbles': int(stat_columns[7].text.strip().replace(',', '')),
                'fumbles_lost': int(stat_columns[8].text.strip().replace(',', ''))
            }
        elif table_title == 'Receiving':
            stats = {
                'receptions': int(stat_columns[1].text.strip().replace(',', '')),
                'receiving_yards': int(stat_columns[3].text.strip().replace(',', '')),
                'reception_average': float(stat_columns[4].text.strip().replace(',', '')),
                'receiving_touchdowns': int(stat_columns[5].text.strip().replace(',', '')),
                'receiving_first_downs': int(stat_columns[7].text.strip().replace(',', '')),
                'receiver_targets': int(stat_columns[2].text.strip().replace(',', '')),
                'receiver_fumbles': int(stat_columns[8].text.strip().replace(',', '')),
                'receiver_fumbles_lost': int(stat_columns[9].text.strip().replace(',', ''))
            }
        elif table_title == 'Kicking':
            stats = {
                'field_goal_ratio': stat_columns[1].text.strip(),
                'field_goal_percentage': stat_columns[2].text.strip(),
                'u_nineteen_fg_ratio': stat_columns[3].text.strip(),
                'u_twentynine_fg_ratio': stat_columns[4].text.strip(),
                'u_thritynine_fg_ratio': stat_columns[5].text.strip(),
                'u_fortynine_fg_ratio': stat_columns[6].text.strip(),
                'o_fifty_fg_ratio': stat_columns[7].text.strip(),
                'field_goal_long': int(stat_columns[8].text.strip().replace(',', '')),
                'extra_points_made': int(stat_columns[9].text.strip().replace(',', '')),
                'extra_point_attempts': int(stat_columns[10].text.strip().replace(',', '')),
                'kicking_points': int(stat_columns[11].text.strip().replace(',', ''))
            }
        
        return stats

    def create_player(self, player_data):
        NFL_Player.objects.create(**player_data)
        self.logger.info(f"Added player: {player_data['player_name']} with PYID: {player_data['PYID']}")

    def get_all_player_ids(self):
        return set(NFL_Player.objects.values_list('PID', flat=True))

    def generate_unique_id(self):
        existing_ids = self.get_all_player_ids()
        while True:
            player_id = random.randint(100000, 999999)
            if player_id not in existing_ids:
                return player_id
