from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import logging
from api.models import MLB_Player, MLB_Team, League, MLB_Game, MLB_Game_link

class Command(BaseCommand):
    help = 'Scrape MLB Game Stats'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        MLB_Game.objects.delete()
        links = set(MLB_Game_link.objects.values_list('link', flat=True))
       
        for link in links:
            self.logger.info(f"Connecting to link {link}")
            driver.get(link)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            game_page = soup.find('div', class_='box')
            if game_page:
                self.scrape_game(game_page)
            else:
                self.logger.error(f"Couldnt find game_page for {link}")
        
        driver.quit()

    def scrape_game(self, game_page):
        team_section = game_page.find('div', class_='scorebox')
        stats_tables = game_page.find_all('div', class_='table_container is_setup')
        year_section = game_page.find('h1').text.strip().split(', ')
        year = year_section[1]
        
        if team_section:
            self.logger.info("Found team section")
        if stats_tables:
            self.logger.info("Found stats")
        else:
            self.logger.info("couldnt find stats")
       
        v_batting_stats = stats_tables[0]
        h_batting_stats = stats_tables[1]
        v_pitching_stats = stats_tables[2]
        h_pitching_stats = stats_tables[3]
        
        self.logger.info("Handling Game")
        self.handle_game(team_section, v_batting_stats, h_batting_stats, v_pitching_stats, h_pitching_stats, year)
        
    def handle_game(self, team_section, v_batting_stats, h_batting_stats, v_pitching_stats, h_pitching_stats, year):
        self.logger.info("handling teams and score")
        GID = self.generate_unique_id()
        LYID = f"MLB_{year}"
        game_and_team_data = self.handle_teams(team_section, year)
        self.logger.info("Scraping visitor batting stats")
        v_batting_data = self.handle_batting_stats(v_batting_stats, year)
        self.logger.info("Scraping home batting stats")
        h_batting_data = self.handle_batting_stats(h_batting_stats, year)
        self.logger.info("Scraping visitor pitching stats")
        v_pitching_data = self.handle_pitching_stats(v_pitching_stats, year)
        self.logger.info("Scraping home pitching stats")
        h_pitching_data = self.handle_pitching_stats(h_pitching_stats, year)

        game_data = self.handle_game_data(LYID, GID, game_and_team_data, v_batting_data, h_batting_data, v_pitching_data, h_pitching_data)

        self.save_game(game_data)

    def handle_teams(self, team_section, year):
        team_name_sections = team_section.find_all('strong')
        team_score_sections = team_section.find_all('div', class_='scores')
        if team_name_sections:
            v_team_section = team_name_sections[0]
            h_team_section = team_name_sections[1]
            v_score_section = team_score_sections[0]
            h_score_section = team_score_sections[1]
            team_data = self.handle_team_sections(v_team_section, h_team_section, v_score_section, h_score_section, year)

            return team_data
        else:
            self.logger.error("Couldnt split v and h team sections")
        
    def handle_team_sections(self, v_team_name_section, h_team_name_section, v_score_section, h_score_section, year):
        v_name= v_team_name_section.find('a').text.strip()
        h_name = h_team_name_section.find('a').text.strip()
        
        if v_name and h_name:
            self.logger.info(f"{v_name} vs {h_name}")
            visitor = self.get_team(v_name, year)
            home = self.get_team(h_name, year)
        else:
            self.logger.error("Couldnt find team names")
        
        v_score_sec = v_score_section.find('div', class_='score')
        h_score_sec = h_score_section.find('div', class_='score')

        if v_score_sec and h_score_sec:
            v_score = int(v_score_sec.text.strip())
            h_score = int(h_score_sec.text.strip())
            score = f"{v_score} - {h_score}"
            if v_score > h_score:
                winner = visitor
            else:
                winner = home
        
        data = self.handle_team_data(home, visitor, winner, score)

        return data
            
    def handle_team_data(self, visitor, home, winner, score):
        data = {
            'home': home,
            'visitor': visitor,
            'winner': winner,
            'score': score
        }
        return data

    def get_team(self, team_name, year):
        try:
            team = MLB_Team.objects.get(team_name=team_name, year=year)
            return team
        except MLB_Team.DoesNotExist:
            self.logger.error(f"Couldnt find team {team_name} in table")
            return None
    
    def to_none(self, value):
        return value if value else None

    def handle_batting_stats(self, table, year):
        if table:  
            player_stats = table.find('tbody')
            team_stats = table.find('tfoot')
            if player_stats and team_stats:
                batting_stats = []
                player_rows = player_stats.find_all('tr')
                team_row = team_stats.find('tr')
                cols = team_row.find_all('td')
                team_stats = {
                    'at_bats': self.to_none(cols[0].text.strip()),
                    'runs': self.to_none(cols[1].text.strip()),
                    'hits': self.to_none(cols[2].text.strip()),
                    'runs_batted_in': self.to_none(cols[3].text.strip()),
                    'walks': self.to_none(cols[4].text.strip()),
                    'strike_outs': self.to_none(cols[5].text.strip()),
                    'batting_average': self.to_none(cols[7].text.strip()),
                    'on_base_percentage': self.to_none(cols[8].text.strip()),
                    'slugging': self.to_none(cols[9].text.strip()),
                    'on_base_plus_slugging': self.to_none(cols[10].text.strip()),
                    'b_pitches': self.to_none(cols[11].text.strip()),
                    'b_strikes': self.to_none(cols[12].text.strip()),
                    'average_leverage_index': self.to_none(cols[14].text.strip()),
                    'win_probability_added': self.to_none(cols[15].text.strip()),
                    'win_probability_subtracted': self.to_none(cols[16].text.strip()),
                    'base_out_runs_added': self.to_none(cols[19].text.strip()),
                    'put_outs': self.to_none(cols[20].text.strip()),
                    'assists': self.to_none(cols[21].text.strip()),
                    'hit_type': self.to_none(cols[22].text.strip())
                }
                batting_stats.append(team_stats)
                for i, row in enumerate(player_rows[:10]):
                    if 'spacer' in row.get('class', []):
                        self.logger.info("Encountered spacer row, stopping.")
                        break
                    stats = self.extract_batting_stats(row, year)
                    batting_stats.append(stats)
                    self.logger.info("Appended stats")
                
                return batting_stats

    def extract_batting_stats(self, row, year):
        name = row.find('th', class_='left').find('a').text.strip()
        player = self.get_player(name, year)
        cols = row.find_all('td')

        stats = {
            'player': player,
            'at_bats': self.to_none(cols[0].text.strip()),
            'runs': self.to_none(cols[1].text.strip()),
            'hits': self.to_none(cols[2].text.strip()),
            'runs_batted_in': self.to_none(cols[3].text.strip()),
            'walks': self.to_none(cols[4].text.strip()),
            'strike_outs': self.to_none(cols[5].text.strip()),
            'batting_average': self.to_none(cols[7].text.strip()),
            'on_base_percentage': self.to_none(cols[8].text.strip()),
            'slugging': self.to_none(cols[9].text.strip()),
            'on_base_plus_slugging': self.to_none(cols[10].text.strip()),
            'pitches': self.to_none(cols[11].text.strip()),
            'strikes': self.to_none(cols[12].text.strip()),
            'average_leverage_index': self.to_none(cols[14].text.strip()),
            'win_probability_added': self.to_none(cols[15].text.strip()),
            'win_probability_subtracted': self.to_none(cols[16].text.strip()),
            'base_out_runs_added': self.to_none(cols[19].text.strip()),
            'put_outs': self.to_none(cols[20].text.strip()),
            'assists': self.to_none(cols[21].text.strip()),
            'hit_type': self.to_none(cols[22].text.strip())
        }
        return stats

    def handle_pitching_stats(self, table, year):
        if table:  
            player_stats = table.find('tbody')
            team_stats = table.find('tfoot')
            if player_stats and team_stats:
                pitching_stats = []
                player_rows = player_stats.find_all('tr')
                team_row = team_stats.find('tr')
                cols = team_row.find_all('td')
                team_stats = {
                    'innings_pitched': self.to_none(cols[0].text.strip()),
                    'hits': self.to_none(cols[1].text.strip()),
                    'runs': self.to_none(cols[2].text.strip()),
                    'earned_runs': self.to_none(cols[3].text.strip()),
                    'walks': self.to_none(cols[4].text.strip()),
                    'strike_outs': self.to_none(cols[5].text.strip()),
                    'home_runs': self.to_none(cols[6].text.strip()),
                    'earned_run_average': self.to_none(cols[7].text.strip()),
                    'batters_faced': self.to_none(cols[8].text.strip()),
                    'p_pitches': self.to_none(cols[9].text.strip()),
                    'p_strikes': self.to_none(cols[10].text.strip()),
                    'gamescore': self.to_none(cols[18].text.strip()),
                    'inherited_runners': self.to_none(cols[19].text.strip()),
                    'inherited_score': self.to_none(cols[20].text.strip()),
                    'win_probablitiy_added': self.to_none(cols[21].text.strip()),
                    'average_leverage_index': self.to_none(cols[22].text.strip()),
                    'base_out_runs_saved': self.to_none(cols[25].text.strip())
                }
                pitching_stats.append(team_stats)
                for i, row in enumerate(player_rows[:8]):
                    stats = self.extract_pitching_stats(row, year)
                    pitching_stats.append(stats)
                    self.logger.info("Appended stats")
                
                return pitching_stats

    def extract_pitching_stats(self, row, year):
        name = row.find('th', class_='left').find('a').text.strip()
        player = self.get_player(name, year)
        cols = row.find_all('td')

        stats = {
            'player': player,
            'innings_pitched': self.to_none(cols[0].text.strip()),
            'hits': self.to_none(cols[1].text.strip()),
            'runs': self.to_none(cols[2].text.strip()),
            'earned_runs': self.to_none(cols[3].text.strip()),
            'walks': self.to_none(cols[4].text.strip()),
            'strike_outs': self.to_none(cols[5].text.strip()),
            'home_runs': self.to_none(cols[6].text.strip()),
            'earned_run_average': self.to_none(cols[7].text.strip()),
            'batters_faced': self.to_none(cols[8].text.strip()),
            'pitches': self.to_none(cols[9].text.strip()),
            'strikes': self.to_none(cols[10].text.strip()),
            'gamescore': self.to_none(cols[18].text.strip()),
            'inherited_runners': self.to_none(cols[19].text.strip()),
            'inherited_score': self.to_none(cols[20].text.strip()),
            'win_probablitiy_added': self.to_none(cols[21].text.strip()),
            'average_leverage_index': self.to_none(cols[22].text.strip()),
            'base_out_runs_saved': self.to_none(cols[25].text.strip())
        }
        return stats


    def handle_game_data(self, LYID, GID, game_and_team_data, v_batting_data, h_batting_data, v_pitching_data, h_pitching_data):
        game_data = {
            'GID': GID,
            'LYID': League.objects.get(LYID=LYID),
            'home': game_and_team_data['home'],
            'visitor': game_and_team_data['visitor'],
            'winner': game_and_team_data['winner'],
            'score': game_and_team_data['score']
        }

        for i in range(1, 11):
            if i <= len(v_batting_data) - 1:
                game_data[f'v_b{i}'] = v_batting_data[i]['player']
                for stat, value in v_batting_data[i].items():
                    if stat != 'player':
                        game_data[f'v_b{i}_{stat}'] = value
            if i <= len(h_batting_data) - 1:
                game_data[f'h_b{i}'] = h_batting_data[i]['player']
                for stat, value in h_batting_data[i].items():
                    if stat != 'player':
                        game_data[f'h_b{i}_{stat}'] = value
            
        for i in range(1, 9):
            if i <= len(h_pitching_data) - 1:
                game_data[f'h_p{i}'] = h_pitching_data[i]['player']
                for stat, value in h_pitching_data[i].items():
                    if stat != 'player':
                        game_data[f'h_p{i}_{stat}'] = value
            if i <= len(v_pitching_data) - 1:
                game_data[f'v_p{i}'] = v_pitching_data[i]['player']
                for stat, value in v_pitching_data[i].items():
                    if stat != 'player':
                        game_data[f'v_p{i}_{stat}'] = value

        for stat, value in h_batting_data[0].items():
            game_data[f'h_{stat}'] = value
        for stat, value in v_batting_data[0].items():
            game_data[f'v_{stat}'] = value
        for stat, value in h_pitching_data[0].items():
            game_data[f'h_{stat}'] = value
        for stat, value in v_pitching_data[0].items():
            game_data[f'v_{stat}'] = value

        return game_data

    def save_game(self, game_data):
        game = MLB_Game(**game_data)
        game.save()

    def get_player(self, player_name, year):
        try:
            name_parts = player_name.split(' ')
            first_name = name_parts[0]
            last_name = name_parts[1]
            query = f"{last_name}, {first_name}"

            player = MLB_Player.objects.get(player_name=query, year=year)
            return player
        except MLB_Player.DoesNotExist:
            self.logger.error(f"Couldn't find player {player_name} in table")
            return None

    def get_all_game_ids(self):
        return set(MLB_Game.objects.values_list('GID', flat=True))

    def generate_unique_id(self):
        existing_ids = self.get_all_game_ids()
        while True:
            game_id = str(random.randint(100000, 999999))
            if game_id not in existing_ids:
                return game_id
