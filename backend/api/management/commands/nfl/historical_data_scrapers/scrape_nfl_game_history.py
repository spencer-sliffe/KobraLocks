from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import logging
from api.models import NFL_Game, NFL_Team, League, NFL_Player

class Command(BaseCommand):
    help = 'Scrape NFL players and populate the player table'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        NFL_Game.objects.all().delete()

        years = [
            "2014", "2015", "2016", "2017", 
            "2018", "2019", "2020", "2021",
            "2022", "2023"
        ]

        teams = {
            "Buffalo Bills": "BUF", "Miami Dolphins": "MIA", "New England Patriots": "NE", "New York Jets": "NYJ",
            "Baltimore Ravens": "BAL", "Cincinnati Bengals": "CIN", "Cleveland Browns": "CLE", "Pittsburgh Steelers": "PIT",
            "Houston Texans": "HOU", "Indianapolis Colts": "IND", "Jacksonville Jaguars": "JAX", "Tennessee Titans": "TEN",
            "Denver Broncos": "DEN", "Kansas City Chiefs": "KC", "Las Vegas Raiders": "LV", "Oakland Raiders": "LV", "San Diego Chargers": "LAC", "Los Angeles Chargers": "LAC",
            "Dallas Cowboys": "DAL", "New York Giants": "NYG", "Philadelphia Eagles": "PHI", "Washington Redskins": "WAS", "Washington Commanders": "WAS",
            "Chicago Bears": "CHI", "Detroit Lions": "DET", "Green Bay Packers": "GB", "Minnesota Vikings": "MIN",
            "Atlanta Falcons": "ATL", "Carolina Panthers": "CAR", "New Orleans Saints": "NO", "Tampa Bay Buccaneers": "TB",
            "St Louis Rams": "LAR", "Arizona Cardinals": "ARI", "Los Angeles Rams": "LAR", "San Francisco 49ers": "SF", "Seattle Seahawks": "SEA"
        }

        for year in years:
            link = f"https://www.sportsoddshistory.com/nfl-game-season/?y={year}"
            self.scrape_season(link, options, teams, year)

    def scrape_season(self, link, options, teams, year):
        self.logger.info(f"Connecting to link {link}")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(link)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        game_section = soup.find('div', class_='site-content')

        if game_section:
            self.logger.info(f"Handling games for year {year}")
            self.process_games(game_section, teams, year, options)
            return
        else:
            self.logger.error(f"Error finding game section for URL: {link}")
        driver.quit()

    def process_games(self, game_section, teams, year, options):
        weekly_game_tables = game_section.find_all('table', class_='soh1')[2:]
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        week = 1

        if weekly_game_tables:
            for weekly_game_table in weekly_game_tables:
                body = weekly_game_table.find_all('tbody')
                if body:
                    game_rows = body[1].find_all('tr')
                    self.logger.info(f"Processing week {week} for year {year}")
                    if game_rows:
                        for game_row in game_rows:
                            game_data, game_team = self.parse_game_data(game_row, teams, year)
                            if game_data and game_team:
                                self.process_player_stats(driver, game_data, game_team, year, week)
                        
                    else:
                        self.logger.error("Error finding game rows")
                week += 1
            return
        else:
            self.logger.error("Error finding weekly game tables")
        driver.quit()

    def parse_game_data(self, game_row, teams, year):
        cols = game_row.find_all('td')
        if cols:
            gid = self.generate_unique_id()

            favorite_name = cols[4].text.strip()
            self.logger.info(f"{favorite_name} is the favorite")
            favorite_team_id = teams.get(favorite_name)
            favorite_tyid = f"{favorite_team_id}_{year}"

            underdog_name = cols[8].text.strip()
            name_parts = underdog_name.split(' ')
            game_team = name_parts[-1]
            self.logger.info(f"Game team: {game_team}")
            underdog_team_id = teams.get(underdog_name)
            underdog_tyid = f"{underdog_team_id}_{year}"

            score_parts = cols[5].text.strip().split(' ')
            score = score_parts[1]

            winner_data = score_parts[0]
            winner = "favorite" if winner_data == "W" else "underdog"

            spread = cols[6].text.strip()
            over_under = cols[9].text.strip()

            data = {
                'GID': gid,
                'LYID': f"NFL_{year}",
                'favorite': favorite_tyid,
                'underdog': underdog_tyid,
                'winner': winner,
                'score': score,
                'spread': spread,
                'over_under': over_under,
                'year': year,
            }
            return data, game_team
        else:
            self.logger.error("Error finding data columns")
        return None, None

    def process_player_stats(self, driver, game_data, game_team, year, week):
        link_template = f"https://sports.yahoo.com/nfl/scoreboard/?confId=&dateRange={week}&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAIcApTRXoSV-Y0_RMsjfee81etEzobyFNt2rYz_PFOLeua8S06mHza-K65eA22ouJiEjqLZgTgw6jw5O2qb6KFwNwE9jj7LwNGFUgK07ucBdTE8xxKFISfiHNuOrdjCrPbKDB5cUZSx-guVxrDeLd4DXbWt8Bios9thwMKxn9J2e&schedState=2&scoreboardSeason={year}"
        driver.get(link_template)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        player_sections = soup.find('ul', class_='D(f) Jc(sb) Flw(w)')
        
        if player_sections:
            player_tables = player_sections.find_all('li', class_='Pos(r) D(ib) W(49%) Mb(20px) Va(t) final Bgc(secondary):h')
            for player_table in player_tables:
                done = self.process_player_table(player_table, game_data, game_team, year, driver)
                if done:
                    return
        else:
            self.logger.error("Error finding player sections")

    def process_player_table(self, player_table, game_data, game_team, year, driver):
        team_section = player_table.find('ul', class_='Mb(3px)')
        if team_section:
            winner_name, loser_name = self.extract_team_names(team_section)
            if loser_name == game_team or winner_name == game_team:
                game_link_section = player_table.find('a', class_='C(primary-text) C(primary-text):link C(primary-text):visited Td(n) gamecard-final')
                if game_link_section:
                    game_link = game_link_section.get('href')
                    full_link = f"https://sports.yahoo.com{game_link}"
                    driver.get(full_link)
                    time.sleep(3)
                    stat_page_soup = BeautifulSoup(driver.page_source, 'html.parser')
                    player_stats_section = stat_page_soup.find('div', class_='player-stats')
                    if player_stats_section:
                        players_data = self.extract_player_stats(player_stats_section, year)
                        game_data.update(players_data)
                        self.create_game_instance(game_data)
                        return True
                else:
                    self.logger.error("Error finding game link section")
        else:
            self.logger.error("Error finding team section")

    def extract_team_names(self, team_section):
        if team_section.find('li', class_='D(tb) team C($c-fuji-grey-f)') and team_section.find('li', class_='D(tb) team Pt(10px)'):
            winner_name = self.get_team_name(team_section, 'D(tb) team Pt(10px)')
            loser_name = self.get_team_name(team_section, 'D(tb) team C($c-fuji-grey-f)')
        elif team_section.find('li', class_='D(tb) team') and team_section.find('li', class_='D(tb) team C($c-fuji-grey-f) Pt(10px)'):
            winner_name = self.get_team_name(team_section, 'D(tb) team')
            loser_name = self.get_team_name(team_section, 'D(tb) team C($c-fuji-grey-f) Pt(10px)')
        elif team_section.find('li', class_='D(tb) team') and team_section.find('li', class_='D(tb) team Pt(10px)'):
            winner_name = self.get_team_name(team_section, 'D(tb) team')
            loser_name = self.get_team_name(team_section, 'D(tb) team Pt(10px)')
        self.logger.info(f"Winner: {winner_name}, Loser: {loser_name}")
        return winner_name, loser_name

    def get_team_name(self, team_section, class_name):
        team_info = team_section.find('li', class_=class_name).find('div', class_='D(tbc) W(80%) Va(m)')
        if team_info:
            team_name_section = team_info.find('span', class_='YahooSans Fw(400)! Fz(12px)!')
            team_name = team_name_section.find('div', class_='Fw(n) Fz(12px)')
            if team_name:
                return team_name.text.strip()
        return None

    def extract_player_stats(self, player_stats_section, year):
        sections = player_stats_section.find_all('div', class_='D(f) Mx(-10px) Jc(sb)')
        team_section = player_stats_section.find('div', class_='D(f) Mx(-10px) Jc(sb) Pt(16px)')
        if sections:
            qb_section = sections[0]
            rb_section = sections[1]
            wr_section = sections[2]
            if qb_section and rb_section and wr_section:
                qb_stats = self.extract_qb_stats(qb_section, year)
                rb_stats = self.extract_rb_stats(rb_section, year)
                wr_stats = self.extract_wr_stats(wr_section, year)
                h_team, v_team = self.extract_teams(team_section, year)
                game_stats = self.handle_data(qb_stats, rb_stats, wr_stats, h_team, v_team)
                return game_stats
            else:
                self.logger.error("Couldn't find position sections")
        else:
            self.logger.error("Couldn't find sections")
        return {}
    
    def extract_teams(self, team_section, year):
        teams_sections = team_section.find_all('div', class_='Mx(10px) D(ib) Ov(a)')
        if teams_sections:
            v_team_name_section = teams_sections[0].find('span', class_='Pstart(15px) Fw(700) Va(m) C(black)')
            h_team_name_section = teams_sections[1].find('span', class_='Pstart(15px) Fw(700) Va(m) C(black)')
            v_team_name = v_team_name_section.text.strip()
            h_team_name = h_team_name_section.text.strip()
            v_team_id = NFL_Team.objects.get(team_name=v_team_name, year=year)
            h_team_id = NFL_Team.objects.get(team_name=h_team_name, year=year)
            v_team = v_team_id.TYID
            h_team = h_team_id.TYID
            return h_team, v_team
        else:
            self.logger.error("Couldn't find team sections")
            return None, None

    def handle_data(self, qb_stats, rb_stats, wr_stats, h_team, v_team):
        data = {
            'h_team': h_team,
            'h_qb': qb_stats['home']['qb'],
            'h_qb_name': qb_stats['home']['qb_name'],
            'h_qb_passing_completions': qb_stats['home']['passing_completions'],
            'h_qb_passing_attempts': qb_stats['home']['passing_attempts'],
            'h_qb_passing_yards': qb_stats['home']['passing_yards'],
            'h_qb_passing_touchdowns': qb_stats['home']['passing_touchdowns'],
            'h_qb_interceptions': qb_stats['home']['interceptions'],
            'h_qb_rating': qb_stats['home']['rating'],

            'h_rb_1': rb_stats['home']['rb_1'],
            'h_rb_1_name': rb_stats['home']['rb_1_name'],
            'h_rb_1_carries': rb_stats['home']['rb_1_carries'],
            'h_rb_1_rushing_yards': rb_stats['home']['rb_1_rushing_yards'],
            'h_rb_1_rush_average': rb_stats['home']['rb_1_rush_average'],
            'h_rb_1_rushing_touchdowns': rb_stats['home']['rb_1_rushing_touchdowns'],
            'h_rb_1_rush_long': rb_stats['home']['rb_1_rush_long'],
            'h_rb_1_fumbles_lost': rb_stats['home']['rb_1_fumbles_lost'],

            'h_rb_2': rb_stats['home']['rb_2'],
            'h_rb_2_name': rb_stats['home']['rb_2_name'],
            'h_rb_2_carries': rb_stats['home']['rb_2_carries'],
            'h_rb_2_rushing_yards': rb_stats['home']['rb_2_rushing_yards'],
            'h_rb_2_rush_average': rb_stats['home']['rb_2_rush_average'],
            'h_rb_2_rushing_touchdowns': rb_stats['home']['rb_2_rushing_touchdowns'],
            'h_rb_2_rush_long': rb_stats['home']['rb_2_rush_long'],
            'h_rb_2_fumbles_lost': rb_stats['home']['rb_2_fumbles_lost'],

            'h_wr_1': wr_stats['home']['wr_1'],
            'h_wr_1_name': wr_stats['home']['wr_1_name'],
            'h_wr_1_receptions': wr_stats['home']['wr_1_receptions'],
            'h_wr_1_receiving_yards': wr_stats['home']['wr_1_receiving_yards'],
            'h_wr_1_reception_average': wr_stats['home']['wr_1_reception_average'],
            'h_wr_1_reception_long': wr_stats['home']['wr_1_reception_long'],
            'h_wr_1_receiving_touchdowns': wr_stats['home']['wr_1_receiving_touchdowns'],
            'h_wr_1_receiving_targets': wr_stats['home']['wr_1_receiving_targets'],
            'h_wr_1_fumbles_lost': wr_stats['home']['wr_1_fumbles_lost'],

            'h_wr_2': wr_stats['home']['wr_2'],
            'h_wr_2_name': wr_stats['home']['wr_2_name'],
            'h_wr_2_receptions': wr_stats['home']['wr_2_receptions'],
            'h_wr_2_receiving_yards': wr_stats['home']['wr_2_receiving_yards'],
            'h_wr_2_reception_average': wr_stats['home']['wr_2_reception_average'],
            'h_wr_2_reception_long': wr_stats['home']['wr_2_reception_long'],
            'h_wr_2_receiving_touchdowns': wr_stats['home']['wr_2_receiving_touchdowns'],
            'h_wr_2_receiving_targets': wr_stats['home']['wr_2_receiving_targets'],
            'h_wr_2_fumbles_lost': wr_stats['home']['wr_2_fumbles_lost'],

            'v_team': v_team,
            'v_qb': qb_stats['visitor']['qb'],
            'v_qb_name': qb_stats['visitor']['qb_name'],
            'v_qb_passing_completions': qb_stats['visitor']['passing_completions'],
            'v_qb_passing_attempts': qb_stats['visitor']['passing_attempts'],
            'v_qb_passing_yards': qb_stats['visitor']['passing_yards'],
            'v_qb_passing_touchdowns': qb_stats['visitor']['passing_touchdowns'],
            'v_qb_interceptions': qb_stats['visitor']['interceptions'],
            'v_qb_rating': qb_stats['visitor']['rating'],

            'v_rb_1': rb_stats['visitor']['rb_1'],
            'v_rb_1_name': rb_stats['visitor']['rb_1_name'],
            'v_rb_1_carries': rb_stats['visitor']['rb_1_carries'],
            'v_rb_1_rushing_yards': rb_stats['visitor']['rb_1_rushing_yards'],
            'v_rb_1_rush_average': rb_stats['visitor']['rb_1_rush_average'],
            'v_rb_1_rushing_touchdowns': rb_stats['visitor']['rb_1_rushing_touchdowns'],
            'v_rb_1_rush_long': rb_stats['visitor']['rb_1_rush_long'],
            'v_rb_1_fumbles_lost': rb_stats['visitor']['rb_1_fumbles_lost'],

            'v_rb_2': rb_stats['visitor']['rb_2'],
            'v_rb_2_name': rb_stats['visitor']['rb_2_name'],
            'v_rb_2_carries': rb_stats['visitor']['rb_2_carries'],
            'v_rb_2_rushing_yards': rb_stats['visitor']['rb_2_rushing_yards'],
            'v_rb_2_rush_average': rb_stats['visitor']['rb_2_rush_average'],
            'v_rb_2_rushing_touchdowns': rb_stats['visitor']['rb_2_rushing_touchdowns'],
            'v_rb_2_rush_long': rb_stats['visitor']['rb_2_rush_long'],
            'v_rb_2_fumbles_lost': rb_stats['visitor']['rb_2_fumbles_lost'],

            'v_wr_1': wr_stats['visitor']['wr_1'],
            'v_wr_1_name': wr_stats['visitor']['wr_1_name'],
            'v_wr_1_receptions': wr_stats['visitor']['wr_1_receptions'],
            'v_wr_1_receiving_yards': wr_stats['visitor']['wr_1_receiving_yards'],
            'v_wr_1_reception_average': wr_stats['visitor']['wr_1_reception_average'],
            'v_wr_1_reception_long': wr_stats['visitor']['wr_1_reception_long'],
            'v_wr_1_receiving_touchdowns': wr_stats['visitor']['wr_1_receiving_touchdowns'],
            'v_wr_1_receiving_targets': wr_stats['visitor']['wr_1_receiving_targets'],
            'v_wr_1_fumbles_lost': wr_stats['visitor']['wr_1_fumbles_lost'],

            'v_wr_2': wr_stats['visitor']['wr_2'],
            'v_wr_2_name': wr_stats['visitor']['wr_2_name'],
            'v_wr_2_receptions': wr_stats['visitor']['wr_2_receptions'],
            'v_wr_2_receiving_yards': wr_stats['visitor']['wr_2_receiving_yards'],
            'v_wr_2_reception_average': wr_stats['visitor']['wr_2_reception_average'],
            'v_wr_2_reception_long': wr_stats['visitor']['wr_2_reception_long'],
            'v_wr_2_receiving_touchdowns': wr_stats['visitor']['wr_2_receiving_touchdowns'],
            'v_wr_2_receiving_targets': wr_stats['visitor']['wr_2_receiving_targets'],
            'v_wr_2_fumbles_lost': wr_stats['visitor']['wr_2_fumbles_lost'],
        }
        return data

    def extract_qb_stats(self, qb_section, year):
        qb_stats = {
            'home': self.get_qb_stats(qb_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[1], year),
            'visitor': self.get_qb_stats(qb_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[0], year)
        }
        return qb_stats

    def extract_rb_stats(self, rb_section, year):
        rb_stats = {
            'home': self.get_rb_stats(rb_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[1], year),
            'visitor': self.get_rb_stats(rb_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[0], year)
        }
        return rb_stats

    def extract_wr_stats(self, wr_section, year):
        wr_stats = {
            'home': self.get_wr_stats(wr_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[1], year),
            'visitor': self.get_wr_stats(wr_section.find_all('div', class_='Mx(10px) D(ib) Ov(a) Va(t) Fx(1) W(100%)')[0], year)
        }
        return wr_stats

    def get_qb_stats(self, qb_stat_section, year):
        if qb_stat_section:
            row = qb_stat_section.find('tbody')
            if row:
                name_section = row.find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                qb, qb_name = self.get_player(name_section, year)
                if not qb:
                    qb = ''
                columns = row.find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')
                if columns:
                    data = {
                        'qb': qb,
                        'qb_name': qb_name,
                        'passing_completions': columns[0].text.strip(),
                        'passing_attempts': columns[1].text.strip(),
                        'passing_yards': columns[2].text.strip(),
                        'passing_touchdowns': columns[3].text.strip(),
                        'interceptions': columns[4].text.strip(),
                        'rating': columns[5].text.strip()
                    }
                    return data 
        else:
            self.logger.error("No QB stat section found")
        return None, None

    def get_rb_stats(self, rb_stat_section, year):
        if rb_stat_section:
            body = rb_stat_section.find('tbody')
            if body:
                rows = body.find_all('tr')
                if rows:
                    if len(rows) > 1:
                        name_section_1 = rows[0].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        name_section_2 = rows[1].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        rb_1, rb_1_name = self.get_player(name_section_1, year)
                        rb_2, rb_2_name = self.get_player(name_section_2, year)
                        if not rb_1:
                            rb_1 = ''
                        if not rb_2:
                            rb_2 = ''
                        rb_1_columns = rows[0].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')
                        rb_2_columns = rows[1].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')

                        data = {
                            'rb_1': rb_1,
                            'rb_1_name': rb_1_name,
                            'rb_1_carries': rb_1_columns[0].text.strip(),
                            'rb_1_rushing_yards': rb_1_columns[1].text.strip(),
                            'rb_1_rush_average': rb_1_columns[2].text.strip(),
                            'rb_1_rushing_touchdowns': rb_1_columns[4].text.strip(),
                            'rb_1_rush_long': rb_1_columns[3].text.strip(),
                            'rb_1_fumbles_lost': rb_1_columns[5].text.strip(),
                            'rb_2': rb_2,
                            'rb_2_name': rb_2_name,
                            'rb_2_carries': rb_2_columns[0].text.strip(),
                            'rb_2_rushing_yards': rb_2_columns[1].text.strip(),
                            'rb_2_rush_average': rb_2_columns[2].text.strip(),
                            'rb_2_rushing_touchdowns': rb_2_columns[4].text.strip(),
                            'rb_2_rush_long': rb_2_columns[3].text.strip(),
                            'rb_2_fumbles_lost': rb_2_columns[5].text.strip(),
                        }
                    else:
                        name_section_1 = rows[0].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        rb_1, rb_1_name = self.get_player(name_section_1, year)
                        if not rb_1:
                            rb_1 = ''
                        
                        rb_1_columns = rows[0].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')

                        data = {
                            'rb_1': rb_1,
                            'rb_1_name': rb_1_name,
                            'rb_1_carries': rb_1_columns[0].text.strip(),
                            'rb_1_rushing_yards': rb_1_columns[1].text.strip(),
                            'rb_1_rush_average': rb_1_columns[2].text.strip(),
                            'rb_1_rushing_touchdowns': rb_1_columns[4].text.strip(),
                            'rb_1_rush_long': rb_1_columns[3].text.strip(),
                            'rb_1_fumbles_lost': rb_1_columns[5].text.strip(),
                            'rb_2': '',
                            'rb_2_name': '',
                            'rb_2_carries': '',
                            'rb_2_rushing_yards': '',
                            'rb_2_rush_average': '',
                            'rb_2_rushing_touchdowns': '',
                            'rb_2_rush_long': '',
                            'rb_2_fumbles_lost': '',
                        }
                    return data
        else:
            self.logger.error("No RB stat section found")
        return [None, None]

    def get_wr_stats(self, wr_stat_section, year):
        if wr_stat_section:
            body = wr_stat_section.find('tbody')
            if body:
                rows = body.find_all('tr')
                if rows:
                    if len(rows) > 1:
                        name_section_1 = rows[0].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        name_section_2 = rows[1].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        wr_1, wr_1_name  = self.get_player(name_section_1, year)
                        wr_2, wr_2_name = self.get_player(name_section_2, year)
                        if not wr_1:
                            wr_1 = ''
                        if not wr_2:
                            wr_2 = ''
                        wr_1_columns = rows[0].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')
                        wr_2_columns = rows[1].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')

                        data = {
                            'wr_1': wr_1,
                            'wr_1_name': wr_1_name,
                            'wr_1_receptions': wr_1_columns[0].text.strip(),
                            'wr_1_receiving_yards': wr_1_columns[1].text.strip(),
                            'wr_1_reception_average': wr_1_columns[2].text.strip(),
                            'wr_1_reception_long': wr_1_columns[3].text.strip(),
                            'wr_1_receiving_touchdowns': wr_1_columns[4].text.strip(),
                            'wr_1_receiving_targets': wr_1_columns[5].text.strip(),
                            'wr_1_fumbles_lost': wr_1_columns[6].text.strip(),
                            'wr_2': wr_2,
                            'wr_2_name': wr_2_name,
                            'wr_2_receptions': wr_2_columns[0].text.strip(),
                            'wr_2_receiving_yards': wr_2_columns[1].text.strip(),
                            'wr_2_reception_average': wr_2_columns[2].text.strip(),
                            'wr_2_reception_long': wr_2_columns[3].text.strip(),
                            'wr_2_receiving_touchdowns': wr_2_columns[4].text.strip(),
                            'wr_2_receiving_targets': wr_2_columns[5].text.strip(),
                            'wr_2_fumbles_lost': wr_2_columns[6].text.strip(),
                        }
                    else:
                        name_section_1 = rows[0].find('th', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(start) Fz(12px) Whs(nw)')
                        wr_1, wr_1_name  = self.get_player(name_section_1, year)
                        if not wr_1:
                            wr_1 = ''
                        wr_1_columns = rows[0].find_all('td', class_='Px(cell-padding-x) Py(cell-padding-y) Va(m) Ta(end) Fz(12px) Whs(nw)')
                        data = {
                            'wr_1': wr_1,
                            'wr_1_name': wr_1_name,
                            'wr_1_receptions': wr_1_columns[0].text.strip(),
                            'wr_1_receiving_yards': wr_1_columns[1].text.strip(),
                            'wr_1_reception_average': wr_1_columns[2].text.strip(),
                            'wr_1_reception_long': wr_1_columns[3].text.strip(),
                            'wr_1_receiving_touchdowns': wr_1_columns[4].text.strip(),
                            'wr_1_receiving_targets': wr_1_columns[5].text.strip(),
                            'wr_1_fumbles_lost': wr_1_columns[6].text.strip(),
                            'wr_2': '',
                            'wr_2_name': '',
                            'wr_2_receptions': '',
                            'wr_2_receiving_yards': '',
                            'wr_2_reception_average': '',
                            'wr_2_reception_long': '',
                            'wr_2_receiving_touchdowns': '',
                            'wr_2_receiving_targets': '',
                            'wr_2_fumbles_lost': '',
                        }
                    return data
        else:
            self.logger.error("No WR stat section found")
            return None

    def get_player(self, section, year):
        name_section = section.find('a', class_='Whs(nw) C(#000) Fw(400)')
        if name_section:
            full_name = name_section.text.strip().split(' ')
            if full_name:
                last_name = full_name[1]
                first_name = full_name[0]
                # Construct player name in the format "Last, First"
                player_name_query = f"{last_name}, {first_name}"
                try:
                    player = NFL_Player.objects.get(player_name=player_name_query, year=year)
                    #player_id = player.
                    pyid = player.PYID
                    return pyid, player_name_query
                except NFL_Player.DoesNotExist:
                    self.logger.info(f"{player_name_query} is not in the database")
                    return None, player_name_query
        else:
            self.logger.error("No player name section found")
        return None, None

    def create_game_instance(self, data):
        try:
            self.logger.info(f"Attempting to create game instance with data: {data}")

            # Fetching necessary objects
            league = League.objects.get(LYID=data['LYID'])
            favorite_team = NFL_Team.objects.get(TYID=data['favorite'])
            underdog_team = NFL_Team.objects.get(TYID=data['underdog'])
            h_team = NFL_Team.objects.get(TYID=data['h_team']) if data['h_team'] else None
            v_team = NFL_Team.objects.get(TYID=data['v_team']) if data['v_team'] else None

            h_qb = NFL_Player.objects.get(PYID=data['h_qb']) if data['h_qb'] else None
            h_rb_1 = NFL_Player.objects.get(PYID=data['h_rb_1']) if data['h_rb_1'] else None
            h_rb_2 = NFL_Player.objects.get(PYID=data['h_rb_2']) if data['h_rb_2'] else None
            h_wr_1 = NFL_Player.objects.get(PYID=data['h_wr_1']) if data['h_wr_1'] else None
            h_wr_2 = NFL_Player.objects.get(PYID=data['h_wr_2']) if data['h_wr_2'] else None

            v_qb = NFL_Player.objects.get(PYID=data['v_qb']) if data['v_qb'] else None
            v_rb_1 = NFL_Player.objects.get(PYID=data['v_rb_1']) if data['v_rb_1'] else None
            v_rb_2 = NFL_Player.objects.get(PYID=data['v_rb_2']) if data['v_rb_2'] else None
            v_wr_1 = NFL_Player.objects.get(PYID=data['v_wr_1']) if data['v_wr_1'] else None
            v_wr_2 = NFL_Player.objects.get(PYID=data['v_wr_2']) if data['v_wr_2'] else None

            game = NFL_Game.objects.create(
                GID=data['GID'],
                LYID=league,
                favorite=favorite_team,
                underdog=underdog_team,
                winner=data['winner'],
                score=data['score'],
                spread=data['spread'],
                over_under=data['over_under'],
                year=data['year'],
                h_team=h_team,
                h_qb=h_qb,
                h_qb_name=data['h_qb_name'],
                h_qb_passing_completions=data['h_qb_passing_completions'],
                h_qb_passing_attempts=data['h_qb_passing_attempts'],
                h_qb_passing_yards=data['h_qb_passing_yards'],
                h_qb_passing_touchdowns=data['h_qb_passing_touchdowns'],
                h_qb_interceptions=data['h_qb_interceptions'],
                h_qb_rating=data['h_qb_rating'],
                h_rb_1=h_rb_1,
                h_rb_1_name=data['h_rb_1_name'],
                h_rb_1_carries=data['h_rb_1_carries'],
                h_rb_1_rushing_yards=data['h_rb_1_rushing_yards'],
                h_rb_1_rush_average=data['h_rb_1_rush_average'],
                h_rb_1_rushing_touchdowns=data['h_rb_1_rushing_touchdowns'],
                h_rb_1_rush_long=data['h_rb_1_rush_long'],
                h_rb_1_fumbles_lost=data['h_rb_1_fumbles_lost'],
                h_rb_2=h_rb_2,
                h_rb_2_name=data['h_rb_2_name'],
                h_rb_2_carries=data['h_rb_2_carries'],
                h_rb_2_rushing_yards=data['h_rb_2_rushing_yards'],
                h_rb_2_rush_average=data['h_rb_2_rush_average'],
                h_rb_2_rushing_touchdowns=data['h_rb_2_rushing_touchdowns'],
                h_rb_2_rush_long=data['h_rb_2_rush_long'],
                h_rb_2_fumbles_lost=data['h_rb_2_fumbles_lost'],
                h_wr_1=h_wr_1,
                h_wr_1_name=data['h_wr_1_name'],
                h_wr_1_receptions=data['h_wr_1_receptions'],
                h_wr_1_receiving_yards=data['h_wr_1_receiving_yards'],
                h_wr_1_reception_average=data['h_wr_1_reception_average'],
                h_wr_1_reception_long=data['h_wr_1_reception_long'],
                h_wr_1_receiving_touchdowns=data['h_wr_1_receiving_touchdowns'],
                h_wr_1_receiving_targets=data['h_wr_1_receiving_targets'],
                h_wr_1_fumbles_lost=data['h_wr_1_fumbles_lost'],
                h_wr_2=h_wr_2,
                h_wr_2_name=data['h_wr_2_name'],
                h_wr_2_receptions=data['h_wr_2_receptions'],
                h_wr_2_receiving_yards=data['h_wr_2_receiving_yards'],
                h_wr_2_reception_average=data['h_wr_2_reception_average'],
                h_wr_2_reception_long=data['h_wr_2_reception_long'],
                h_wr_2_receiving_touchdowns=data['h_wr_2_receiving_touchdowns'],
                h_wr_2_receiving_targets=data['h_wr_2_receiving_targets'],
                h_wr_2_fumbles_lost=data['h_wr_2_fumbles_lost'],
                v_team=v_team,
                v_qb=v_qb,
                v_qb_name=data['v_qb_name'],
                v_qb_passing_completions=data['v_qb_passing_completions'],
                v_qb_passing_attempts=data['v_qb_passing_attempts'],
                v_qb_passing_yards=data['v_qb_passing_yards'],
                v_qb_passing_touchdowns=data['v_qb_passing_touchdowns'],
                v_qb_interceptions=data['v_qb_interceptions'],
                v_qb_rating=data['v_qb_rating'],
                v_rb_1=v_rb_1,
                v_rb_1_name=data['v_rb_1_name'],
                v_rb_1_carries=data['v_rb_1_carries'],
                v_rb_1_rushing_yards=data['v_rb_1_rushing_yards'],
                v_rb_1_rush_average=data['v_rb_1_rush_average'],
                v_rb_1_rushing_touchdowns=data['v_rb_1_rushing_touchdowns'],
                v_rb_1_rush_long=data['v_rb_1_rush_long'],
                v_rb_1_fumbles_lost=data['v_rb_1_fumbles_lost'],
                v_rb_2=v_rb_2,
                v_rb_2_name=data['v_rb_2_name'],
                v_rb_2_carries=data['v_rb_2_carries'],
                v_rb_2_rushing_yards=data['v_rb_2_rushing_yards'],
                v_rb_2_rush_average=data['v_rb_2_rush_average'],
                v_rb_2_rushing_touchdowns=data['v_rb_2_rushing_touchdowns'],
                v_rb_2_rush_long=data['v_rb_2_rush_long'],
                v_rb_2_fumbles_lost=data['v_rb_2_fumbles_lost'],
                v_wr_1=v_wr_1,
                v_wr_1_name=data['v_wr_1_name'],
                v_wr_1_receptions=data['v_wr_1_receptions'],
                v_wr_1_receiving_yards=data['v_wr_1_receiving_yards'],
                v_wr_1_reception_average=data['v_wr_1_reception_average'],
                v_wr_1_reception_long=data['v_wr_1_reception_long'],
                v_wr_1_receiving_touchdowns=data['v_wr_1_receiving_touchdowns'],
                v_wr_1_receiving_targets=data['v_wr_1_receiving_targets'],
                v_wr_1_fumbles_lost=data['v_wr_1_fumbles_lost'],
                v_wr_2=v_wr_2,
                v_wr_2_name=data['v_wr_2_name'],
                v_wr_2_receptions=data['v_wr_2_receptions'],
                v_wr_2_receiving_yards=data['v_wr_2_receiving_yards'],
                v_wr_2_reception_average=data['v_wr_2_reception_average'],
                v_wr_2_reception_long=data['v_wr_2_reception_long'],
                v_wr_2_receiving_touchdowns=data['v_wr_2_receiving_touchdowns'],
                v_wr_2_receiving_targets=data['v_wr_2_receiving_targets'],
                v_wr_2_fumbles_lost=data['v_wr_2_fumbles_lost'],
            )

            self.logger.info(f"Created game instance: {game.GID}")

        except League.DoesNotExist:
            self.logger.error(f"League with LYID {data['LYID']} does not exist.")
        except NFL_Team.DoesNotExist as e:
            self.logger.error(f"Team does not exist: {e}")
        except NFL_Player.DoesNotExist as e:
            self.logger.error(f"Player does not exist: {e}")
        except Exception as e:
            self.logger.error(f"Error creating game instance: {e}")

    def get_all_game_ids(self):
        return set(NFL_Game.objects.values_list('GID', flat=True))

    def generate_unique_id(self):
        existing_ids = self.get_all_game_ids()
        while True:
            game_id = random.randint(100000, 999999)
            if game_id not in existing_ids:
                return game_id
