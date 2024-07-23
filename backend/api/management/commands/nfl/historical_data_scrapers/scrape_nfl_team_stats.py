#https://www.espn.com/nfl/team/stats/_/name/{TID}/season/{year}/seasontype/2

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from api.models import NFL_Team

class Command(BaseCommand):
    help = 'Scraping NFL players to put them into the player table'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        teams = {
            "wsh"
        }
        years = {
            "2014", "2015", "2016", "2017", 
            "2018", "2019", "2020", "2021",
            "2022", "2023"
        }

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for team in teams:
                for year in years:
                    link = f"https://www.espn.com/nfl/team/stats/_/type/team/name/{team}/season/{year}/seasontype/2"
                    futures.append(executor.submit(self.scrape_team, link, options, team, year))
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    self.logger.error(f"Generated an exception: {exc}")

    def scrape_team(self, link, options, team, year):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        try:
            self.logger.info(f"Connecting to link {link}")
            driver.get(link)
            time.sleep(3)  # Wait for the page to load
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            stats_section = soup.find('section', class_='Card')
            standing_section = soup.find('div', class_='ResponsiveWrapper')

            if stats_section and standing_section:
                self.logger.info(f"Handling team")
                self.handle_team(stats_section, standing_section, team, year)
            else:
                self.logger.error(f"Error finding stat section or header for URL: {link}")
        finally:
            driver.quit()

    def handle_team(self, stats_section, standing_section, team, year):
        # team id
        tyid = f"WAS_{year}"
        nfl_team = NFL_Team.objects.get(TYID=tyid)
        self.logger.info(f"handling team: {tyid}")
        # team standing
        # division_standing = self.scrape_team_standing(standing_section)
        data_array = self.scrape_team_stats(stats_section)
        data = self.handle_stats(data_array)
        if data:
            team_data = data
            self.logger.info(f"{data}")
            self.update_team_with_stats(nfl_team, team_data)


    def scrape_team_stats(self, stats_section):
        table_section = stats_section.find('table', class_='Table Table--align-right')
        table_body = table_section.find('tbody', class_='Table__TBODY')
        data_rows = table_body.select('tr.filled.Table__TR.Table__TR--sm.Table__even, tr.Table__TR.Table__TR--sm.Table__even')

        values = []
        for row in data_rows:
            data_elements = row.find_all('td', class_='Table__TD')
            for data_element in data_elements:
                data = data_element.text.strip()
                # Check if the data is an integer with commas
                if ',' in data:
                    try:
                        # Try to convert the data to an integer after removing commas
                        data = int(data.replace(',', ''))
                    except ValueError:
                        pass  # If conversion fails, keep the data as is
                if data != '':
                    values.append(data)
        self.logger.info(f"data values found: {values}")
        return values

    def handle_stats(self, data):
        stats = {
            'total_points_per_game': data[0],
            'total_points': data[2],
            'total_touchdowns': data[4],
            'total_1st_downs': data[6],
            'rushing_first_downs': data[8],
            'passing_first_downs': data[10],
            'first_downs_by_penalty': data[12],
            'third_down_efficiency': data[14],
            'third_down_percentage': data[16],
            'fourth_down_efficiency': data[18],
            'fourth_down_percentage': data[20],
            'passing_completions_to_attempts': data[22],
            'net_passing_yards': data[24],
            'yards_per_pass_attempt': data[26],
            'net_passing_yards_per_game': data[28],
            'passing_touchdowns': data[30],
            'interceptions': data[32],
            'sacks_to_yards_lost': data[34],
            'rushing_attempts': data[36],
            'rushing_yards': data[38],
            'yards_per_rush_attempt': data[40],
            'rushing_yards_per_game': data[42],
            'rushing_touchdowns': data[44],
            'total_offensive_plays': data[46],
            'total_yards': data[48],
            'yards_per_game': data[50],
            'kickoff_returns_to_yards': data[52],
            'average_kickoff_return_yards': data[54],
            'punt_returns_to_yards': data[56],
            'average_punt_return_yards': data[58],
            'interception_returns_to_yards': data[60],
            'average_interception_yards': data[62],
            'fieldgoal_makes_to_attempts': data[68],
            'total_penalties_to_yards': data[72],
            'average_penalty_yards_per_game': data[74],
            'time_of_possession': data[76],
            'fumbles_to_fumbles_lost': data[78],
            'turnover_ratio': data[80],

            # Opponents
            'o_total_points_per_game': data[1],
            'o_total_points': data[3],
            'o_total_touchdowns': data[5],
            'o_total_1st_downs': data[7],
            'o_rushing_first_downs': data[9],
            'o_passing_first_downs': data[11],
            'o_first_downs_by_penalty': data[13],
            'o_third_down_efficiency': data[15],
            'o_third_down_percentage': data[17],
            'o_fourth_down_efficiency': data[19],
            'o_fourth_down_percentage': data[21],
            'o_passing_completions_to_attempts': data[23],
            'o_net_passing_yards': data[25],
            'o_yards_per_pass_attempt': data[27],
            'o_net_passing_yards_per_game': data[29],
            'o_passing_touchdowns': data[31],
            'o_interceptions': data[33],
            'o_sacks_to_yards_lost': data[35],
            'o_rushing_attempts': data[37],
            'o_rushing_yards': data[39],
            'o_yards_per_rush_attempt': data[41],
            'o_rushing_yards_per_game': data[43],
            'o_rushing_touchdowns': data[45],
            'o_total_offensive_plays': data[47],
            'o_total_yards': data[49],
            'o_yards_per_game': data[51],
            'o_kickoff_returns_to_yards': data[53],
            'o_average_kickoff_return_yards': data[55],
            'o_punt_returns_to_yards': data[57],
            'o_average_punt_return_yards': data[59],
            'o_interception_returns_to_yards': data[61],
            'o_average_interception_yards': data[63],
            'o_fieldgoal_makes_to_attempts': data[69],
            'o_total_penalties_to_yards': data[73],
            'o_average_penalty_yards_per_game': data[75],
            'o_time_of_possession': data[77],
            'o_fumbles_to_fumbles_lost': data[79],
            'o_turnover_ratio': data[81]
        }
        return stats

    def update_team_with_stats(self, nfl_team, team_data):
        for key, value in team_data.items():
            setattr(nfl_team, key, value)
        nfl_team.save()
        self.logger.info(f"Updated team {nfl_team.TYID} with stats for the year {nfl_team.year}")
            