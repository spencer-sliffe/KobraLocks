from django.db import models
from django.contrib.auth.models import User
import json

#Baseball
class NCAABBGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    inning_state = models.CharField(max_length=50, null=True, blank=True)  # Combined inning state
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    balls = models.IntegerField(null=True, blank=True)
    strikes = models.IntegerField(null=True, blank=True)
    outs = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class NCAABBFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title
    
class MLBGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    inning_state = models.CharField(max_length=50, null=True, blank=True)  # Combined inning state
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    balls = models.IntegerField(null=True, blank=True)
    strikes = models.IntegerField(null=True, blank=True)
    outs = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class MLBFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title


class MLBSpecials(models.Model):
    section_title = models.CharField(max_length=100)
    bet_titles = models.TextField()
    odds = models.TextField()

    def set_bet_titles(self, bet_titles_list):
        self.bet_titles = json.dumps(bet_titles_list)

    def get_bet_titles(self):
        return json.loads(self.bet_titles)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class MLBPlayerFutures(models.Model):
    section_title = models.CharField(max_length=100)
    players = models.TextField()
    odds = models.TextField()

    def set_players(self, players_list):
        self.teams = json.dumps(players_list)

    def get_players(self):
        return json.loads(self.players)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title
    
class MLBTeamPlayoffs(models.Model):
    row_title = models.CharField(max_length=100)
    yes_odds = models.CharField(max_length=20, null=True, blank=True)
    no_odds = models.CharField(max_length=20, null=True, blank=True)

class MLBWinTotals(models.Model):
    team = models.CharField(max_length=100)
    over_title = models.CharField(max_length=100)
    under_title = models.CharField(max_length=100)
    over_odds = models.CharField(max_length=20, null=True, blank=True)
    under_odds = models.CharField(max_length=20, null=True, blank=True)

class MLBGameLinks(models.Model):
    links = models.TextField()
    
    def set_links(self, links_list):
        self.links = json.dumps(links_list)

    def get_links(self):
        return json.loads(self.links)

class MLBGameParlays(models.Model):
    game_id = models.CharField(max_length=100, null=True, blank=True)
    game = models.CharField(max_length=100, null=True, blank=True)
    section_title = models.CharField(max_length=100)
    player = models.CharField(max_length=50, null=True, blank=True)
    decimal_odds = models.TextField()
    american_odds = models.TextField()

    def set_decimal_odds(self, decimal_odds_list):
        self.teams = json.dumps(decimal_odds_list)

    def get_decimal_odds(self):
        return json.loads(self.decimal_odds)

    def set_american_odds(self, american_odds_list):
        self.american_odds = json.dumps(american_odds_list)

    def get_american_odds(self):
        return json.loads(self.american_odds)

class MLBGameProps(models.Model):
    game_id = models.CharField(max_length=100, null=True, blank=True)
    game = models.CharField(max_length=100, null=True, blank=True)
    section_title = models.CharField(max_length=100)
    row_title = models.CharField(max_length=100)
    decimal_odds = models.TextField()
    american_odds = models.TextField()

    def set_decimal_odds(self, decimal_odds_list):
        self.teams = json.dumps(decimal_odds_list)

    def get_decimal_odds(self):
        return json.loads(self.decimal_odds)

    def set_american_odds(self, american_odds_list):
        self.american_odds = json.dumps(american_odds_list)

    def get_american_odds(self):
        return json.loads(self.american_odds)

class MLBGamePlayerProps(models.Model):
    game_id = models.CharField(max_length=100, null=True, blank=True)
    game = models.CharField(max_length=100, null=True, blank=True)
    section_title = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    row_title = models.CharField(max_length=100)
    decimal_odds = models.TextField()
    american_odds = models.TextField()

    def set_decimal_odds(self, decimal_odds_list):
        self.teams = json.dumps(decimal_odds_list)

    def get_decimal_odds(self):
        return json.loads(self.decimal_odds)

    def set_american_odds(self, american_odds_list):
        self.american_odds = json.dumps(american_odds_list)

    def get_american_odds(self):
        return json.loads(self.american_odds)

class MLBGameSpecials(models.Model):
    game_id = models.CharField(max_length=100, null=True, blank=True)
    game = models.CharField(max_length=100, null=True, blank=True)
    section_title = models.CharField(max_length=100)
    row_value = models.CharField(max_length=20, null=True, blank=True)
    odds = models.CharField(max_length=20, null=True, blank=True)

# Football
class NFLGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class NFLFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class NFLPlayerFutures(models.Model):
    section_title = models.CharField(max_length=100)
    players = models.TextField()
    odds = models.TextField()

    def set_players(self, players_list):
        self.teams = json.dumps(players_list)

    def get_players(self):
        return json.loads(self.players)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class NFLPlayerTotals(models.Model):
    row_title = models.CharField(max_length=100)
    over_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    under_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    over_american_odds = models.CharField(max_length=20, null=True, blank=True)
    under_american_odds = models.CharField(max_length=20, null=True, blank=True)

class NFLDivisionSpecials(models.Model):
    section_title = models.CharField(max_length=100)
    bet_titles = models.TextField(null=True)
    team_titles = models.TextField(null=True)
    odds = models.TextField()
    
    def set_team_titles(self, team_titles_list):
        self.team_titles = json.dumps(team_titles_list)

    def get_team_titles(self):
        return json.loads(self.team_titles)

    def set_bet_titles(self, bet_titles_list):
        self.bet_titles = json.dumps(bet_titles_list)

    def get_bet_titles(self):
        return json.loads(self.bet_titles)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class NFLSeasonSpecials(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title
    
class NCAAFBGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

# Basketball
class NCAABaskBallGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class NBAGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class NBAFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class NBAPlayerFutures(models.Model):
    section_title = models.CharField(max_length=100)
    players = models.TextField()
    odds = models.TextField()

    def set_players(self, players_list):
        self.teams = json.dumps(players_list)

    def get_players(self):
        return json.loads(self.players)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title
    
class WNBAGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class WNBAFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class WNBAPlayerFutures(models.Model):
    section_title = models.CharField(max_length=100)
    players = models.TextField()
    odds = models.TextField()

    def set_players(self, players_list):
        self.teams = json.dumps(players_list)

    def get_players(self):
        return json.loads(self.players)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title
# Soccer
class MLSGame(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    team1_record = models.CharField(max_length=100)
    team2_record = models.CharField(max_length=100)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)  
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_odds = models.CharField(max_length=20, null=True, blank=True)
    draw_odds = models.CharField(max_length=20, null=True, blank=True)
    team2_odds = models.CharField(max_length=20, null=True, blank=True) 

class MLSFutures(models.Model):
    section_title = models.CharField(max_length=100)
    teams = models.TextField()  # Store JSON-encoded list as a string
    odds = models.TextField()   # Store JSON-encoded list as a string

    def set_teams(self, teams_list):
        self.teams = json.dumps(teams_list)

    def get_teams(self):
        return json.loads(self.teams)

    def set_odds(self, odds_list):
        self.odds = json.dumps(odds_list)

    def get_odds(self):
        return json.loads(self.odds)

    def __str__(self):
        return self.section_title

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)