from django.db import models
from django.contrib.auth.models import User
import json

from django.db import models

# Leagues

class League(models.Model):
    LID = models.CharField(max_length=10)  # League ID like MLB, NFL, etc.
    LYID = models.CharField(max_length=10, primary_key=True)  # League Year ID
    year = models.PositiveIntegerField()
    bias = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.LID

class Game(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    GID = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.GID
    
class Team(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    TID = models.CharField(max_length=10, primary_key=True) 
    def __str__(self):
        return self.TID

class Bet(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    BID = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.BID

class Scheduled_Game(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    GID = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.CharField(max_length=20, null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    live = models.BooleanField(default=False)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class Live_Game(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    GID =  models.ForeignKey(Game, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game_time = models.CharField(max_length=50, null=True, blank=True)  
    team1_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_spread = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_total = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team1_money = models.CharField(max_length=20, null=True, blank=True)  # Increased size
    team2_money = models.CharField(max_length=20, null=True, blank=True)
    quarter_state = models.CharField(max_length=50, null=True, blank=True)
    half_state = models.CharField(max_length=50, null=True, blank=True)
    inning_state = models.CharField(max_length=50, null=True, blank=True)
    clock = models.CharField(max_length=50, null=True, blank=True)
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    home_time_outs = models.IntegerField(null=True, blank=True)
    away_time_outs = models.IntegerField(null=True, blank=True)
    
class Available_Bet(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    BID = models.ForeignKey(Bet, on_delete=models.CASCADE)
    ABID = models.CharField(max_length=10, primary_key=True)   

class Game_Bet(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    BID =  models.ForeignKey(Bet, on_delete=models.CASCADE)
    ABID = models.ForeignKey(Available_Bet, on_delete=models.CASCADE)
    GBID = models.CharField(max_length=10, primary_key=True)
    bet_type = models.CharField(null=True, blank=True) 
    bet_description = models.CharField(null=True, blank=True) 
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.CharField(null=True, blank=True) 
    statistic = models.CharField(null=True, blank=True)               # outcome, home run, score
    statistic_value = models.CharField(null=True, blank=True)          # win/loss, +-2, +-7
    spread_min = 
    spread_max = 
    decimal_over = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    decimal_under = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    american_over = models.CharField(null=True, blank=True)    
    american_under = models.CharField(null=True, blank=True) 

class Season_Bet(models.Model):
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)
    BID =  models.ForeignKey(Bet, on_delete=models.CASCADE)
    ABID = models.ForeignKey(Available_Bet, on_delete=models.CASCADE)
    SBID = models.CharField(max_length=10, primary_key=True)
    bet_type = models.CharField(null=True, blank=True) 
    bet_description = models.CharField(null=True, blank=True) 
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.CharField(null=True, blank=True) 
    statistic = models.CharField(null=True, blank=True)               # outcome, home run, score
    statistic_value = models.CharField(null=True, blank=True)          # win/loss, +-2, +-7
    decimal_over = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    decimal_under = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    american_over = models.CharField(null=True, blank=True)    
    american_under = models.CharField(null=True, blank=True) 

# NFL

class NFL_Team(models.Model):
    TID = models.CharField(max_length=10)  # Universal team identifier
    TYID = models.CharField(max_length=10, primary_key=True)  # Team identifier for a specific year
    LYID = models.ForeignKey(League, on_delete=models.CASCADE, related_name='nfl_teams')  # League Year ID as a foreign key
    DYID = models.ForeignKey('NFL_Division', on_delete=models.CASCADE, related_name='nfl_teams')  # Conference Year ID as a foreign key
    team_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    record = models.CharField(max_length=15, null=True, blank=True)
    division_standing = models.CharField(max_length=30, null=True, blank=True)
    # Team
    total_points_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    total_points = models.IntegerField(null=True, blank=True)
    total_touchdowns = models.IntegerField(null=True, blank=True)
    total_1st_downs = models.IntegerField(null=True, blank=True)
    rushing_first_downs = models.IntegerField(null=True, blank=True)
    passing_first_downs = models.IntegerField(null=True, blank=True)
    first_downs_by_penalty = models.IntegerField(null=True, blank=True)
    third_down_efficiency = models.CharField(max_length=15, null=True, blank=True)
    third_down_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fourth_down_efficiency = models.CharField(max_length=15, null=True, blank=True)
    fourth_down_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    passing_completions_to_attempts = models.CharField(max_length=15, null=True, blank=True)
    net_passing_yards = models.IntegerField(null=True, blank=True)
    yards_per_pass_attempt = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    net_passing_yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    passing_touchdowns = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    sacks_to_yards_lost = models.CharField(max_length=15, null=True, blank=True)
    rushing_attempts = models.IntegerField(null=True, blank=True)
    rushing_yards = models.IntegerField(null=True, blank=True)
    yards_per_rush_attempt = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    rushing_yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    rushing_touchdowns = models.IntegerField(null=True, blank=True)
    total_offensive_plays = models.IntegerField(null=True, blank=True)
    total_yards = models.IntegerField(null=True, blank=True)
    yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    kickoff_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    average_kickoff_return_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    punt_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    average_punt_return_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    interception_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    average_interception_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    fieldgoal_makes_to_attempts = models.CharField(max_length=15, null=True, blank=True)
    total_penalties_to_yards = models.CharField(max_length=15, null=True, blank=True)
    average_penalty_yards_per_game = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    time_of_possession = models.CharField(max_length=15, null=True, blank=True)
    fumbles_to_fumbles_lost = models.CharField(max_length=15, null=True, blank=True)
    turnover_ratio = models.CharField(max_length=15, null=True, blank=True)

    # Opponents
    o_total_points_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_total_points = models.IntegerField(null=True, blank=True)
    o_total_touchdowns = models.IntegerField(null=True, blank=True)
    o_total_1st_downs = models.IntegerField(null=True, blank=True)
    o_rushing_first_downs = models.IntegerField(null=True, blank=True)
    o_passing_first_downs = models.IntegerField(null=True, blank=True)
    o_first_downs_by_penalty = models.IntegerField(null=True, blank=True)
    o_third_down_efficiency = models.CharField(max_length=15, null=True, blank=True)
    o_third_down_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    o_fourth_down_efficiency = models.CharField(max_length=15, null=True, blank=True)
    o_fourth_down_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    o_passing_completions_to_attempts = models.CharField(max_length=15, null=True, blank=True)
    o_net_passing_yards = models.IntegerField(null=True, blank=True)
    o_yards_per_pass_attempt = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_net_passing_yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_passing_touchdowns = models.IntegerField(null=True, blank=True)
    o_interceptions = models.IntegerField(null=True, blank=True)
    o_sacks_to_yards_lost = models.CharField(max_length=15, null=True, blank=True)
    o_rushing_attempts = models.IntegerField(null=True, blank=True)
    o_rushing_yards = models.IntegerField(null=True, blank=True)
    o_yards_per_rush_attempt = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_rushing_yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_rushing_touchdowns = models.IntegerField(null=True, blank=True)
    o_total_offensive_plays = models.IntegerField(null=True, blank=True)
    o_total_yards = models.IntegerField(null=True, blank=True)
    o_yards_per_game = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_kickoff_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    o_average_kickoff_return_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_punt_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    o_average_punt_return_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_interception_returns_to_yards = models.CharField(max_length=15, null=True, blank=True)
    o_average_interception_yards = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    o_fieldgoal_makes_to_attempts = models.CharField(max_length=15, null=True, blank=True)
    o_total_penalties_to_yards = models.CharField(max_length=15, null=True, blank=True)
    o_average_penalty_yards_per_game = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    o_time_of_possession = models.CharField(max_length=15, null=True, blank=True)
    o_fumbles_to_fumbles_lost = models.CharField(max_length=15, null=True, blank=True)
    o_turnover_ratio = models.CharField(max_length=15, null=True, blank=True)

class NFL_Division(models.Model):
    DID = models.CharField(max_length=10, null=True, blank=True)
    LYID = models.ForeignKey(League, on_delete=models.CASCADE, related_name='nfl_conferences')
    DYID = models.CharField(max_length=15, primary_key=True)  # Team identifier for a specific year
    first_place = models.ForeignKey(NFL_Team, related_name='first_place_in_conference', on_delete=models.CASCADE, null=True, blank=True)
    second_place = models.ForeignKey(NFL_Team, related_name='second_place_in_conference', on_delete=models.CASCADE, null=True, blank=True)
    third_place = models.ForeignKey(NFL_Team, related_name='third_place_in_conference', on_delete=models.CASCADE, null=True, blank=True)
    fourth_place = models.ForeignKey(NFL_Team, related_name='fourth_place_in_conference', on_delete=models.CASCADE, null=True, blank=True)

class NFL_Player(models.Model):
    PID = models.CharField(max_length=10)  # Universal player identifier
    PYID = models.CharField(max_length=20, primary_key=True)  # Player identifier for a specific year
    TYID = models.ForeignKey(NFL_Team, on_delete=models.CASCADE, related_name='players')  # Team ID the player played on for that year
    DYID = models.ForeignKey(NFL_Division, on_delete=models.CASCADE, related_name='players')  # Conference Year ID as a foreign key
    LYID = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True, related_name='players')  # League Year ID as a foreign key
    player_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    link = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=4, null=True, blank=True)
    games_played = models.IntegerField(null=True, blank=True)

    # QB
    pass_attempts = models.IntegerField(null=True, blank=True)
    pass_completions = models.IntegerField(null=True, blank=True)
    completion_percentage = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    passing_yards = models.IntegerField(null=True, blank=True)
    yards_per_attempt = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    passing_touchdowns = models.IntegerField(null=True, blank=True)
    interceptions = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    sacks = models.IntegerField(null=True, blank=True)
    QB_rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

    # Rushing
    rushing_attempts = models.IntegerField(null=True, blank=True)
    rushing_yards = models.IntegerField(null=True, blank=True)
    rushing_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    rushing_touchdowns = models.IntegerField(null=True, blank=True)
    rushing_first_downs = models.IntegerField(null=True, blank=True)
    fumbles = models.IntegerField(null=True, blank=True)
    fumbles_lost = models.IntegerField(null=True, blank=True)

    # Receiving
    receptions = models.IntegerField(null=True, blank=True)
    receiving_yards = models.IntegerField(null=True, blank=True)
    reception_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    receiving_touchdowns = models.IntegerField(null=True, blank=True)
    receiving_first_downs = models.IntegerField(null=True, blank=True)
    receiver_targets = models.IntegerField(null=True, blank=True)
    receiver_fumbles = models.IntegerField(null=True, blank=True)
    receiver_fumbles_lost = models.IntegerField(null=True, blank=True)
    
    # Kicking
    field_goal_ratio =  models.CharField(max_length=15, null=True, blank=True)
    field_goal_percentage = models.CharField(max_length=15, null=True, blank=True)
    u_nineteen_fg_ratio = models.CharField(max_length=15, null=True, blank=True)
    u_twentynine_fg_ratio = models.CharField(max_length=15, null=True, blank=True)
    u_thritynine_fg_ratio = models.CharField(max_length=15, null=True, blank=True)
    u_fortynine_fg_ratio = models.CharField(max_length=15, null=True, blank=True)
    o_fifty_fg_ratio = models.CharField(max_length=15, null=True, blank=True)
    field_goal_long = models.IntegerField(null=True, blank=True)
    extra_points_made = models.IntegerField(null=True, blank=True)
    extra_point_attempts = models.IntegerField(null=True, blank=True)
    kicking_points = models.IntegerField(null=True, blank=True)

class NFL_player_link(models.Model):
    link = models.CharField(max_length=100)

class NFL_Game(models.Model):
    GID = models.CharField(max_length=10)
    LYID = models.ForeignKey(League, on_delete=models.CASCADE) 
    favorite = models.ForeignKey(NFL_Team, related_name='favorite_team', on_delete=models.CASCADE, null=True, blank=True)
    underdog = models.ForeignKey(NFL_Team, related_name='underdog_team', on_delete=models.CASCADE, null=True, blank=True)
    winner = models.CharField(max_length=10, null=True, blank=True) 
    score = models.CharField(max_length=10, null=True, blank=True) 
    spread = models.CharField(max_length=10, null=True, blank=True) 
    over_under = models.CharField(max_length=10, null=True, blank=True) 
    year = models.CharField(max_length=10, null=True, blank=True) 
    
    h_team = models.ForeignKey(NFL_Team, related_name='h_team', on_delete=models.CASCADE, null=True, blank=True)
    h_qb = models.ForeignKey(NFL_Player, related_name='h_qb', on_delete=models.CASCADE, null=True, blank=True)
    h_qb_name = models.CharField(max_length=60, null=True, blank=True) 
    h_qb_passing_completions = models.IntegerField(null=True, blank=True)
    h_qb_passing_attempts = models.IntegerField(null=True, blank=True)
    h_qb_passing_yards = models.IntegerField(null=True, blank=True)
    h_qb_passing_touchdowns = models.IntegerField(null=True, blank=True)
    h_qb_interceptions = models.IntegerField(null=True, blank=True)
    h_qb_rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    h_rb_1_name = models.CharField(max_length=60, null=True, blank=True) 
    h_rb_1 = models.ForeignKey(NFL_Player, related_name='h_rb_1', on_delete=models.CASCADE, null=True, blank=True)
    h_rb_1_carries = models.IntegerField(null=True, blank=True)
    h_rb_1_rushing_yards = models.IntegerField(null=True, blank=True)
    h_rb_1_rush_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    h_rb_1_rushing_touchdowns = models.IntegerField(null=True, blank=True)
    h_rb_1_rush_long = models.IntegerField(null=True, blank=True)
    h_rb_1_fumbles_lost = models.IntegerField(null=True, blank=True)
    h_wr_1_name = models.CharField(max_length=60, null=True, blank=True) 
    h_wr_1 = models.ForeignKey(NFL_Player, related_name='h_wr_1', on_delete=models.CASCADE, null=True, blank=True)
    h_wr_1_receptions = models.IntegerField(null=True, blank=True)
    h_wr_1_receiving_yards = models.IntegerField(null=True, blank=True)
    h_wr_1_reception_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    h_wr_1_reception_long = models.IntegerField(null=True, blank=True)
    h_wr_1_receiving_touchdowns = models.IntegerField(null=True, blank=True)
    h_wr_1_receiving_targets = models.IntegerField(null=True, blank=True)
    h_wr_1_fumbles_lost = models.IntegerField(null=True, blank=True)
    h_rb_2_name = models.CharField(max_length=60, null=True, blank=True) 
    h_rb_2 = models.ForeignKey(NFL_Player, related_name='h_rb_2', on_delete=models.CASCADE, null=True, blank=True)
    h_rb_2_carries = models.IntegerField(null=True, blank=True)
    h_rb_2_rushing_yards = models.IntegerField(null=True, blank=True)
    h_rb_2_rush_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    h_rb_2_rushing_touchdowns = models.IntegerField(null=True, blank=True)
    h_rb_2_rush_long = models.IntegerField(null=True, blank=True)
    h_rb_2_fumbles_lost = models.IntegerField(null=True, blank=True)
    h_wr_2_name = models.CharField(max_length=60, null=True, blank=True) 
    h_wr_2 = models.ForeignKey(NFL_Player, related_name='h_wr_2', on_delete=models.CASCADE, null=True, blank=True)
    h_wr_2_receptions = models.IntegerField(null=True, blank=True)
    h_wr_2_receiving_yards = models.IntegerField(null=True, blank=True)
    h_wr_2_reception_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    h_wr_2_reception_long = models.IntegerField(null=True, blank=True)
    h_wr_2_receiving_touchdowns = models.IntegerField(null=True, blank=True)
    h_wr_2_receiving_targets = models.IntegerField(null=True, blank=True)
    h_wr_2_fumbles_lost = models.IntegerField(null=True, blank=True)

    v_team = models.ForeignKey(NFL_Team, related_name='v_team', on_delete=models.CASCADE, null=True, blank=True)
    v_qb_name = models.CharField(max_length=60, null=True, blank=True) 
    v_qb = models.ForeignKey(NFL_Player, related_name='v_qb', on_delete=models.CASCADE, null=True, blank=True)
    v_qb_passing_completions = models.IntegerField(null=True, blank=True)
    v_qb_passing_attempts = models.IntegerField(null=True, blank=True)
    v_qb_passing_yards = models.IntegerField(null=True, blank=True)
    v_qb_passing_touchdowns = models.IntegerField(null=True, blank=True)
    v_qb_interceptions = models.IntegerField(null=True, blank=True)
    v_qb_rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    v_rb_1_name = models.CharField(max_length=60, null=True, blank=True) 
    v_rb_1 = models.ForeignKey(NFL_Player, related_name='v_rb_1', on_delete=models.CASCADE, null=True, blank=True)
    v_rb_1_carries = models.IntegerField(null=True, blank=True)
    v_rb_1_rushing_yards = models.IntegerField(null=True, blank=True)
    v_rb_1_rush_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    v_rb_1_rushing_touchdowns = models.IntegerField(null=True, blank=True)
    v_rb_1_rush_long = models.IntegerField(null=True, blank=True)
    v_rb_1_fumbles_lost = models.IntegerField(null=True, blank=True)
    v_wr_1_name = models.CharField(max_length=60, null=True, blank=True) 
    v_wr_1 = models.ForeignKey(NFL_Player, related_name='v_wr_1', on_delete=models.CASCADE, null=True, blank=True)
    v_wr_1_receptions = models.IntegerField(null=True, blank=True)
    v_wr_1_receiving_yards = models.IntegerField(null=True, blank=True)
    v_wr_1_reception_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    v_wr_1_reception_long = models.IntegerField(null=True, blank=True)
    v_wr_1_receiving_touchdowns = models.IntegerField(null=True, blank=True)
    v_wr_1_receiving_targets = models.IntegerField(null=True, blank=True)
    v_wr_1_fumbles_lost = models.IntegerField(null=True, blank=True)
    v_rb_2_name = models.CharField(max_length=60, null=True, blank=True) 
    v_rb_2 = models.ForeignKey(NFL_Player, related_name='v_rb_2', on_delete=models.CASCADE, null=True, blank=True)
    v_rb_2_carries = models.IntegerField(null=True, blank=True)
    v_rb_2_rushing_yards = models.IntegerField(null=True, blank=True)
    v_rb_2_rush_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    v_rb_2_rushing_touchdowns = models.IntegerField(null=True, blank=True)
    v_rb_2_rush_long = models.IntegerField(null=True, blank=True)
    v_rb_2_fumbles_lost = models.IntegerField(null=True, blank=True)
    v_wr_2_name = models.CharField(max_length=60, null=True, blank=True) 
    v_wr_2 = models.ForeignKey(NFL_Player, related_name='v_wr_2', on_delete=models.CASCADE, null=True, blank=True)
    v_wr_2_receptions = models.IntegerField(null=True, blank=True)
    v_wr_2_receiving_yards = models.IntegerField(null=True, blank=True)
    v_wr_2_reception_average = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    v_wr_2_reception_long = models.IntegerField(null=True, blank=True)
    v_wr_2_receiving_touchdowns = models.IntegerField(null=True, blank=True)
    v_wr_2_receiving_targets = models.IntegerField(null=True, blank=True)
    v_wr_2_fumbles_lost = models.IntegerField(null=True, blank=True)

#NFL Bets




class NFL_Future(models.Model):
    #teams and odds are parallel arrays
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

class NFL_Player_Future(models.Model):
    # players and odds are parallel arrays
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

class NFL_Player_Total(models.Model):
    row_title = models.CharField(max_length=100)
    over_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    under_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    over_american_odds = models.CharField(max_length=20, null=True, blank=True)
    under_american_odds = models.CharField(max_length=20, null=True, blank=True)

class NFL_Division_Special(models.Model):
    # bet titles (if not null) and odds are parallel arrays
    # team title (if not null) and odds are parallel arrays 
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

class NFL_Season_Special(models.Model):
    # teams and odds are parallel arrays
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
    
# MLB
class MLB_Team(models.Model):
    TID = models.CharField(max_length=10)  # Universal team identifier
    TYID = models.CharField(max_length=10, primary_key=True)  # Team identifier for a specific year
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)  # League Year ID as a foreign key
    team_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    games = models.PositiveIntegerField()
    # Batting
    at_bats = models.IntegerField(null=True, blank=True)
    runs = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    doubles = models.IntegerField(null=True, blank=True)
    triples = models.IntegerField(null=True, blank=True)
    home_runs = models.IntegerField(null=True, blank=True)
    runs_batted_in = models.IntegerField(null=True, blank=True)
    walks = models.IntegerField(null=True, blank=True)
    strike_outs = models.IntegerField(null=True, blank=True)
    stolen_bases = models.IntegerField(null=True, blank=True)
    caught_stealing = models.IntegerField(null=True, blank=True)
    batting_average = models.DecimalField(max_digits=5, decimal_places=3)
    on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3)
    slugging_percentage = models.DecimalField(max_digits=5, decimal_places=3)
    on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3)
    # Pitching
    wins = models.IntegerField(null=True, blank=True)
    losses = models.IntegerField(null=True, blank=True)
    earned_run_average = models.DecimalField(max_digits=5, decimal_places=2)
    shut_outs = models.IntegerField(null=True, blank=True)
    holds = models.IntegerField(null=True, blank=True)
    saves = models.IntegerField(null=True, blank=True)
    save_opportunities = models.IntegerField(null=True, blank=True)
    p_hits = models.IntegerField(null=True, blank=True)
    p_runs = models.IntegerField(null=True, blank=True)
    earned_runs = models.IntegerField(null=True, blank=True)
    p_home_runs = models.IntegerField(null=True, blank=True)
    p_walks = models.IntegerField(null=True, blank=True)
    p_strike_outs = models.IntegerField(null=True, blank=True) 
    whip = models.DecimalField(max_digits=5, decimal_places=2) 
    batting_average_against = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.team_name

class MLB_Player(models.Model):
    PID = models.CharField(max_length=10)  # Universal player identifier
    PYID = models.CharField(max_length=20, primary_key=True)  # Player identifier for a specific year
    TYID = models.ForeignKey(MLB_Team, on_delete=models.CASCADE)  # Team ID the player played on for that year
    LYID = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True)   # League Year ID as a foreign key
    player_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    link = models.CharField(max_length=100, null=True, blank=True) 
    # Batting
    at_bats = models.IntegerField(null=True, blank=True)
    runs = models.IntegerField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    total_bases = models.IntegerField(null=True, blank=True)
    doubles = models.IntegerField(null=True, blank=True)
    triples = models.IntegerField(null=True, blank=True)
    home_runs = models.IntegerField(null=True, blank=True)
    runs_batted_in = models.IntegerField(null=True, blank=True)
    walks = models.IntegerField(null=True, blank=True)
    strike_outs = models.IntegerField(null=True, blank=True)
    stolen_bases = models.IntegerField(null=True, blank=True)
    caught_stealing = models.IntegerField(null=True, blank=True)
    batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    slugging_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    # Fielding
    position = models.CharField(max_length=5, null=True, blank=True)  
    games = models.IntegerField(null=True, blank=True)
    errors = models.IntegerField(null=True, blank=True)
    double_plays = models.IntegerField(null=True, blank=True)
    fielding_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    # Pitching
    wins = models.IntegerField(null=True, blank=True)
    losses = models.IntegerField(null=True, blank=True)
    earned_run_average = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    p_games = models.IntegerField(null=True, blank=True)
    games_started = models.IntegerField(null=True, blank=True)
    complete_games = models.IntegerField(null=True, blank=True)
    shut_outs = models.IntegerField(null=True, blank=True)
    holds = models.IntegerField(null=True, blank=True)
    saves = models.IntegerField(null=True, blank=True)
    save_opportunities = models.IntegerField(null=True, blank=True)
    innings_pitched = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    p_hits = models.IntegerField(null=True, blank=True)
    p_runs = models.IntegerField(null=True, blank=True)
    earned_runs = models.IntegerField(null=True, blank=True)
    p_home_runs = models.IntegerField(null=True, blank=True)
    number_of_pitches = models.IntegerField(null=True, blank=True)
    p_walks = models.IntegerField(null=True, blank=True)
    p_strike_outs = models.IntegerField(null=True, blank=True) 
    whip = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    batting_average_against = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.player_name

class MLB_Game(models.Model):
    GID = models.CharField(max_length=10, primary_key=True)  # Universal game ID
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)  # League Year ID as a foreign key
    home = models.ForeignKey(MLB_Team, related_name='home_games', on_delete=models.CASCADE)  # Home team's team ID
    visitor = models.ForeignKey(MLB_Team, related_name='away_games', on_delete=models.CASCADE)  # Visiting team's team ID
    winner =  models.ForeignKey(MLB_Team, related_name='winning_games', on_delete=models.CASCADE)
    score = models.CharField(max_length=20, null=True, blank=True)  

    h_b1 = models.ForeignKey(MLB_Player, related_name='home_batter_1', on_delete=models.CASCADE, null=True, blank=True)
    h_b2 = models.ForeignKey(MLB_Player, related_name='home_batter_2', on_delete=models.CASCADE, null=True, blank=True)
    h_b3 = models.ForeignKey(MLB_Player, related_name='home_batter_3', on_delete=models.CASCADE, null=True, blank=True)
    h_b4 = models.ForeignKey(MLB_Player, related_name='home_batter_4', on_delete=models.CASCADE, null=True, blank=True)
    h_b5 = models.ForeignKey(MLB_Player, related_name='home_batter_5', on_delete=models.CASCADE, null=True, blank=True)
    h_b6 = models.ForeignKey(MLB_Player, related_name='home_batter_6', on_delete=models.CASCADE, null=True, blank=True)
    h_b7 = models.ForeignKey(MLB_Player, related_name='home_batter_7', on_delete=models.CASCADE, null=True, blank=True)
    h_b8 = models.ForeignKey(MLB_Player, related_name='home_batter_8', on_delete=models.CASCADE, null=True, blank=True)
    h_b9 = models.ForeignKey(MLB_Player, related_name='home_batter_9', on_delete=models.CASCADE, null=True, blank=True)
    h_b10 = models.ForeignKey(MLB_Player, related_name='home_batter_10', on_delete=models.CASCADE, null=True, blank=True)

    v_b1 = models.ForeignKey(MLB_Player, related_name='visitor_batter_1', on_delete=models.CASCADE, null=True, blank=True)
    v_b2 = models.ForeignKey(MLB_Player, related_name='visitor_batter_2', on_delete=models.CASCADE, null=True, blank=True)
    v_b3 = models.ForeignKey(MLB_Player, related_name='visitor_batter_3', on_delete=models.CASCADE, null=True, blank=True)
    v_b4 = models.ForeignKey(MLB_Player, related_name='visitor_batter_4', on_delete=models.CASCADE, null=True, blank=True)
    v_b5 = models.ForeignKey(MLB_Player, related_name='visitor_batter_5', on_delete=models.CASCADE, null=True, blank=True)
    v_b6 = models.ForeignKey(MLB_Player, related_name='visitor_batter_6', on_delete=models.CASCADE, null=True, blank=True)
    v_b7 = models.ForeignKey(MLB_Player, related_name='visitor_batter_7', on_delete=models.CASCADE, null=True, blank=True)
    v_b8 = models.ForeignKey(MLB_Player, related_name='visitor_batter_8', on_delete=models.CASCADE, null=True, blank=True)
    v_b9 = models.ForeignKey(MLB_Player, related_name='visitor_batter_9', on_delete=models.CASCADE, null=True, blank=True)
    v_b10 = models.ForeignKey(MLB_Player, related_name='visitor_batter_10', on_delete=models.CASCADE, null=True, blank=True)

    h_p1 = models.ForeignKey(MLB_Player, related_name='home_pitcher_1', on_delete=models.CASCADE, null=True, blank=True)
    h_p2 = models.ForeignKey(MLB_Player, related_name='home_pitcher_2', on_delete=models.CASCADE, null=True, blank=True)
    h_p3 = models.ForeignKey(MLB_Player, related_name='home_pitcher_3', on_delete=models.CASCADE, null=True, blank=True)
    h_p4 = models.ForeignKey(MLB_Player, related_name='home_pitcher_4', on_delete=models.CASCADE, null=True, blank=True)
    h_p5 = models.ForeignKey(MLB_Player, related_name='home_pitcher_5', on_delete=models.CASCADE, null=True, blank=True)
    h_p6 = models.ForeignKey(MLB_Player, related_name='home_pitcher_6', on_delete=models.CASCADE, null=True, blank=True)
    h_p7 = models.ForeignKey(MLB_Player, related_name='home_pitcher_7', on_delete=models.CASCADE, null=True, blank=True)
    h_p8 = models.ForeignKey(MLB_Player, related_name='home_pitcher_8', on_delete=models.CASCADE, null=True, blank=True)

    v_p1 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_1', on_delete=models.CASCADE, null=True, blank=True)
    v_p2 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_2', on_delete=models.CASCADE, null=True, blank=True)
    v_p3 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_3', on_delete=models.CASCADE, null=True, blank=True)
    v_p4 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_4', on_delete=models.CASCADE, null=True, blank=True)
    v_p5 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_5', on_delete=models.CASCADE, null=True, blank=True)
    v_p6 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_6', on_delete=models.CASCADE, null=True, blank=True)
    v_p7 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_7', on_delete=models.CASCADE, null=True, blank=True)
    v_p8 = models.ForeignKey(MLB_Player, related_name='visitor_pitcher_8', on_delete=models.CASCADE, null=True, blank=True)

    h_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_hits = models.IntegerField(null=True, blank=True)
    h_runs = models.IntegerField(null=True, blank=True)
    h_earned_runs = models.IntegerField(null=True, blank=True)
    h_walks = models.IntegerField(null=True, blank=True)
    h_strike_outs = models.IntegerField(null=True, blank=True)
    h_home_runs = models.IntegerField(null=True, blank=True)
    h_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_batters_faced = models.IntegerField(null=True, blank=True)
    h_p_pitches = models.IntegerField(null=True, blank=True)
    h_p_strikes = models.IntegerField(null=True, blank=True)
    h_gamescore = models.IntegerField(null=True, blank=True)
    h_inherited_runners = models.IntegerField(null=True, blank=True)
    h_inherited_score= models.IntegerField(null=True, blank=True)
    h_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_hits = models.IntegerField(null=True, blank=True)
    v_runs = models.IntegerField(null=True, blank=True)
    v_earned_runs = models.IntegerField(null=True, blank=True)
    v_walks = models.IntegerField(null=True, blank=True)
    v_strike_outs = models.IntegerField(null=True, blank=True)
    v_home_runs = models.IntegerField(null=True, blank=True)
    v_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_batters_faced = models.IntegerField(null=True, blank=True)
    v_p_pitches = models.IntegerField(null=True, blank=True)
    v_p_strikes = models.IntegerField(null=True, blank=True)
    v_gamescore = models.IntegerField(null=True, blank=True)
    v_inherited_runners = models.IntegerField(null=True, blank=True)
    v_inherited_score= models.IntegerField(null=True, blank=True)
    v_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p1_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p1_hits = models.IntegerField(null=True, blank=True)
    h_p1_runs = models.IntegerField(null=True, blank=True)
    h_p1_earned_runs = models.IntegerField(null=True, blank=True)
    h_p1_walks = models.IntegerField(null=True, blank=True)
    h_p1_strike_outs = models.IntegerField(null=True, blank=True)
    h_p1_home_runs = models.IntegerField(null=True, blank=True)
    h_p1_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p1_batters_faced = models.IntegerField(null=True, blank=True)
    h_p1_pitches = models.IntegerField(null=True, blank=True)
    h_p1_strikes = models.IntegerField(null=True, blank=True)
    h_p1_gamescore = models.IntegerField(null=True, blank=True)
    h_p1_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p1_inherited_score= models.IntegerField(null=True, blank=True)
    h_p1_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p1_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p1_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p2_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p2_hits = models.IntegerField(null=True, blank=True)
    h_p2_runs = models.IntegerField(null=True, blank=True)
    h_p2_earned_runs = models.IntegerField(null=True, blank=True)
    h_p2_walks = models.IntegerField(null=True, blank=True)
    h_p2_strike_outs = models.IntegerField(null=True, blank=True)
    h_p2_home_runs = models.IntegerField(null=True, blank=True)
    h_p2_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p2_batters_faced = models.IntegerField(null=True, blank=True)
    h_p2_pitches = models.IntegerField(null=True, blank=True)
    h_p2_strikes = models.IntegerField(null=True, blank=True)
    h_p2_gamescore = models.IntegerField(null=True, blank=True)
    h_p2_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p2_inherited_score= models.IntegerField(null=True, blank=True)
    h_p2_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p2_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p2_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p3_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p3_hits = models.IntegerField(null=True, blank=True)
    h_p3_runs = models.IntegerField(null=True, blank=True)
    h_p3_earned_runs = models.IntegerField(null=True, blank=True)
    h_p3_walks = models.IntegerField(null=True, blank=True)
    h_p3_strike_outs = models.IntegerField(null=True, blank=True)
    h_p3_home_runs = models.IntegerField(null=True, blank=True)
    h_p3_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p3_batters_faced = models.IntegerField(null=True, blank=True)
    h_p3_pitches = models.IntegerField(null=True, blank=True)
    h_p3_strikes = models.IntegerField(null=True, blank=True)
    h_p3_gamescore = models.IntegerField(null=True, blank=True)
    h_p3_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p3_inherited_score= models.IntegerField(null=True, blank=True)
    h_p3_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p3_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p3_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p4_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p4_hits = models.IntegerField(null=True, blank=True)
    h_p4_runs = models.IntegerField(null=True, blank=True)
    h_p4_earned_runs = models.IntegerField(null=True, blank=True)
    h_p4_walks = models.IntegerField(null=True, blank=True)
    h_p4_strike_outs = models.IntegerField(null=True, blank=True)
    h_p4_home_runs = models.IntegerField(null=True, blank=True)
    h_p4_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p4_batters_faced = models.IntegerField(null=True, blank=True)
    h_p4_pitches = models.IntegerField(null=True, blank=True)
    h_p4_strikes = models.IntegerField(null=True, blank=True)
    h_p4_gamescore = models.IntegerField(null=True, blank=True)
    h_p4_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p4_inherited_score= models.IntegerField(null=True, blank=True)
    h_p4_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p4_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p4_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p5_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p5_hits = models.IntegerField(null=True, blank=True)
    h_p5_runs = models.IntegerField(null=True, blank=True)
    h_p5_earned_runs = models.IntegerField(null=True, blank=True)
    h_p5_walks = models.IntegerField(null=True, blank=True)
    h_p5_strike_outs = models.IntegerField(null=True, blank=True)
    h_p5_home_runs = models.IntegerField(null=True, blank=True)
    h_p5_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p5_batters_faced = models.IntegerField(null=True, blank=True)
    h_p5_pitches = models.IntegerField(null=True, blank=True)
    h_p5_strikes = models.IntegerField(null=True, blank=True)
    h_p5_gamescore = models.IntegerField(null=True, blank=True)
    h_p5_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p5_inherited_score= models.IntegerField(null=True, blank=True)
    h_p5_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p5_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p5_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p6_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p6_hits = models.IntegerField(null=True, blank=True)
    h_p6_runs = models.IntegerField(null=True, blank=True)
    h_p6_earned_runs = models.IntegerField(null=True, blank=True)
    h_p6_walks = models.IntegerField(null=True, blank=True)
    h_p6_strike_outs = models.IntegerField(null=True, blank=True)
    h_p6_home_runs = models.IntegerField(null=True, blank=True)
    h_p6_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p6_batters_faced = models.IntegerField(null=True, blank=True)
    h_p6_pitches = models.IntegerField(null=True, blank=True)
    h_p6_strikes = models.IntegerField(null=True, blank=True)
    h_p6_gamescore = models.IntegerField(null=True, blank=True)
    h_p6_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p6_inherited_score= models.IntegerField(null=True, blank=True)
    h_p6_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p6_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p6_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p7_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p7_hits = models.IntegerField(null=True, blank=True)
    h_p7_runs = models.IntegerField(null=True, blank=True)
    h_p7_earned_runs = models.IntegerField(null=True, blank=True)
    h_p7_walks = models.IntegerField(null=True, blank=True)
    h_p7_strike_outs = models.IntegerField(null=True, blank=True)
    h_p7_home_runs = models.IntegerField(null=True, blank=True)
    h_p7_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p7_batters_faced = models.IntegerField(null=True, blank=True)
    h_p7_pitches = models.IntegerField(null=True, blank=True)
    h_p7_strikes = models.IntegerField(null=True, blank=True)
    h_p7_gamescore = models.IntegerField(null=True, blank=True)
    h_p7_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p7_inherited_score= models.IntegerField(null=True, blank=True)
    h_p7_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p7_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p7_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_p8_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p8_hits = models.IntegerField(null=True, blank=True)
    h_p8_runs = models.IntegerField(null=True, blank=True)
    h_p8_earned_runs = models.IntegerField(null=True, blank=True)
    h_p8_walks = models.IntegerField(null=True, blank=True)
    h_p8_strike_outs = models.IntegerField(null=True, blank=True)
    h_p8_home_runs = models.IntegerField(null=True, blank=True)
    h_p8_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    h_p8_batters_faced = models.IntegerField(null=True, blank=True)
    h_p8_pitches = models.IntegerField(null=True, blank=True)
    h_p8_strikes = models.IntegerField(null=True, blank=True)
    h_p8_gamescore = models.IntegerField(null=True, blank=True)
    h_p8_inherited_runners = models.IntegerField(null=True, blank=True)
    h_p8_inherited_score= models.IntegerField(null=True, blank=True)
    h_p8_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p8_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_p8_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p1_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p1_hits = models.IntegerField(null=True, blank=True)
    v_p1_runs = models.IntegerField(null=True, blank=True)
    v_p1_earned_runs = models.IntegerField(null=True, blank=True)
    v_p1_walks = models.IntegerField(null=True, blank=True)
    v_p1_strike_outs = models.IntegerField(null=True, blank=True)
    v_p1_home_runs = models.IntegerField(null=True, blank=True)
    v_p1_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p1_batters_faced = models.IntegerField(null=True, blank=True)
    v_p1_pitches = models.IntegerField(null=True, blank=True)
    v_p1_strikes = models.IntegerField(null=True, blank=True)
    v_p1_gamescore = models.IntegerField(null=True, blank=True)
    v_p1_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p1_inherited_score= models.IntegerField(null=True, blank=True)
    v_p1_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p1_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p1_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p2_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p2_hits = models.IntegerField(null=True, blank=True)
    v_p2_runs = models.IntegerField(null=True, blank=True)
    v_p2_earned_runs = models.IntegerField(null=True, blank=True)
    v_p2_walks = models.IntegerField(null=True, blank=True)
    v_p2_strike_outs = models.IntegerField(null=True, blank=True)
    v_p2_home_runs = models.IntegerField(null=True, blank=True)
    v_p2_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p2_batters_faced = models.IntegerField(null=True, blank=True)
    v_p2_pitches = models.IntegerField(null=True, blank=True)
    v_p2_strikes = models.IntegerField(null=True, blank=True)
    v_p2_gamescore = models.IntegerField(null=True, blank=True)
    v_p2_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p2_inherited_score= models.IntegerField(null=True, blank=True)
    v_p2_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p2_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p2_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p3_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p3_hits = models.IntegerField(null=True, blank=True)
    v_p3_runs = models.IntegerField(null=True, blank=True)
    v_p3_earned_runs = models.IntegerField(null=True, blank=True)
    v_p3_walks = models.IntegerField(null=True, blank=True)
    v_p3_strike_outs = models.IntegerField(null=True, blank=True)
    v_p3_home_runs = models.IntegerField(null=True, blank=True)
    v_p3_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p3_batters_faced = models.IntegerField(null=True, blank=True)
    v_p3_pitches = models.IntegerField(null=True, blank=True)
    v_p3_strikes = models.IntegerField(null=True, blank=True)
    v_p3_gamescore = models.IntegerField(null=True, blank=True)
    v_p3_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p3_inherited_score= models.IntegerField(null=True, blank=True)
    v_p3_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p3_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p3_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p4_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p4_hits = models.IntegerField(null=True, blank=True)
    v_p4_runs = models.IntegerField(null=True, blank=True)
    v_p4_earned_runs = models.IntegerField(null=True, blank=True)
    v_p4_walks = models.IntegerField(null=True, blank=True)
    v_p4_strike_outs = models.IntegerField(null=True, blank=True)
    v_p4_home_runs = models.IntegerField(null=True, blank=True)
    v_p4_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p4_batters_faced = models.IntegerField(null=True, blank=True)
    v_p4_pitches = models.IntegerField(null=True, blank=True)
    v_p4_strikes = models.IntegerField(null=True, blank=True)
    v_p4_gamescore = models.IntegerField(null=True, blank=True)
    v_p4_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p4_inherited_score= models.IntegerField(null=True, blank=True)
    v_p4_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p4_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p4_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p5_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p5_hits = models.IntegerField(null=True, blank=True)
    v_p5_runs = models.IntegerField(null=True, blank=True)
    v_p5_earned_runs = models.IntegerField(null=True, blank=True)
    v_p5_walks = models.IntegerField(null=True, blank=True)
    v_p5_strike_outs = models.IntegerField(null=True, blank=True)
    v_p5_home_runs = models.IntegerField(null=True, blank=True)
    v_p5_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p5_batters_faced = models.IntegerField(null=True, blank=True)
    v_p5_pitches = models.IntegerField(null=True, blank=True)
    v_p5_strikes = models.IntegerField(null=True, blank=True)
    v_p5_gamescore = models.IntegerField(null=True, blank=True)
    v_p5_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p5_inherited_score= models.IntegerField(null=True, blank=True)
    v_p5_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p5_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p5_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p6_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p6_hits = models.IntegerField(null=True, blank=True)
    v_p6_runs = models.IntegerField(null=True, blank=True)
    v_p6_earned_runs = models.IntegerField(null=True, blank=True)
    v_p6_walks = models.IntegerField(null=True, blank=True)
    v_p6_strike_outs = models.IntegerField(null=True, blank=True)
    v_p6_home_runs = models.IntegerField(null=True, blank=True)
    v_p6_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p6_batters_faced = models.IntegerField(null=True, blank=True)
    v_p6_pitches = models.IntegerField(null=True, blank=True)
    v_p6_strikes = models.IntegerField(null=True, blank=True)
    v_p6_gamescore = models.IntegerField(null=True, blank=True)
    v_p6_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p6_inherited_score= models.IntegerField(null=True, blank=True)
    v_p6_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p6_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p6_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p7_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p7_hits = models.IntegerField(null=True, blank=True)
    v_p7_runs = models.IntegerField(null=True, blank=True)
    v_p7_earned_runs = models.IntegerField(null=True, blank=True)
    v_p7_walks = models.IntegerField(null=True, blank=True)
    v_p7_strike_outs = models.IntegerField(null=True, blank=True)
    v_p7_home_runs = models.IntegerField(null=True, blank=True)
    v_p7_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p7_batters_faced = models.IntegerField(null=True, blank=True)
    v_p7_pitches = models.IntegerField(null=True, blank=True)
    v_p7_strikes = models.IntegerField(null=True, blank=True)
    v_p7_gamescore = models.IntegerField(null=True, blank=True)
    v_p7_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p7_inherited_score= models.IntegerField(null=True, blank=True)
    v_p7_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p7_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p7_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    v_p8_innings_pitched = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p8_hits = models.IntegerField(null=True, blank=True)
    v_p8_runs = models.IntegerField(null=True, blank=True)
    v_p8_earned_runs = models.IntegerField(null=True, blank=True)
    v_p8_walks = models.IntegerField(null=True, blank=True)
    v_p8_strike_outs = models.IntegerField(null=True, blank=True)
    v_p8_home_runs = models.IntegerField(null=True, blank=True)
    v_p8_earned_run_average = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    v_p8_batters_faced = models.IntegerField(null=True, blank=True)
    v_p8_pitches = models.IntegerField(null=True, blank=True)
    v_p8_strikes = models.IntegerField(null=True, blank=True)
    v_p8_gamescore = models.IntegerField(null=True, blank=True)
    v_p8_inherited_runners = models.IntegerField(null=True, blank=True)
    v_p8_inherited_score= models.IntegerField(null=True, blank=True)
    v_p8_win_probablitiy_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p8_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_p8_base_out_runs_saved = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    h_b1_at_bats = models.IntegerField(null=True, blank=True)
    h_b1_runs = models.IntegerField(null=True, blank=True)
    h_b1_hits = models.IntegerField(null=True, blank=True)
    h_b1_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b1_walks = models.IntegerField(null=True, blank=True)
    h_b1_strike_outs = models.IntegerField(null=True, blank=True)
    h_b1_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_pitches = models.IntegerField(null=True, blank=True)
    h_b1_strikes = models.IntegerField(null=True, blank=True)
    h_b1_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b1_put_outs = models.IntegerField(null=True, blank=True)
    h_b1_assists = models.IntegerField(null=True, blank=True)
    h_b1_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b2_at_bats = models.IntegerField(null=True, blank=True)
    h_b2_runs = models.IntegerField(null=True, blank=True)
    h_b2_hits = models.IntegerField(null=True, blank=True)
    h_b2_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b2_walks = models.IntegerField(null=True, blank=True)
    h_b2_strike_outs = models.IntegerField(null=True, blank=True)
    h_b2_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_pitches = models.IntegerField(null=True, blank=True)
    h_b2_strikes = models.IntegerField(null=True, blank=True)
    h_b2_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b2_put_outs = models.IntegerField(null=True, blank=True)
    h_b2_assists = models.IntegerField(null=True, blank=True)
    h_b2_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b3_at_bats = models.IntegerField(null=True, blank=True)
    h_b3_runs = models.IntegerField(null=True, blank=True)
    h_b3_hits = models.IntegerField(null=True, blank=True)
    h_b3_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b3_walks = models.IntegerField(null=True, blank=True)
    h_b3_strike_outs = models.IntegerField(null=True, blank=True)
    h_b3_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_pitches = models.IntegerField(null=True, blank=True)
    h_b3_strikes = models.IntegerField(null=True, blank=True)
    h_b3_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b3_put_outs = models.IntegerField(null=True, blank=True)
    h_b3_assists = models.IntegerField(null=True, blank=True)
    h_b3_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b4_at_bats = models.IntegerField(null=True, blank=True)
    h_b4_runs = models.IntegerField(null=True, blank=True)
    h_b4_hits = models.IntegerField(null=True, blank=True)
    h_b4_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b4_walks = models.IntegerField(null=True, blank=True)
    h_b4_strike_outs = models.IntegerField(null=True, blank=True)
    h_b4_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_pitches = models.IntegerField(null=True, blank=True)
    h_b4_strikes = models.IntegerField(null=True, blank=True)
    h_b4_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b4_put_outs = models.IntegerField(null=True, blank=True)
    h_b4_assists = models.IntegerField(null=True, blank=True)
    h_b4_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b5_at_bats = models.IntegerField(null=True, blank=True)
    h_b5_runs = models.IntegerField(null=True, blank=True)
    h_b5_hits = models.IntegerField(null=True, blank=True)
    h_b5_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b5_walks = models.IntegerField(null=True, blank=True)
    h_b5_strike_outs = models.IntegerField(null=True, blank=True)
    h_b5_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_pitches = models.IntegerField(null=True, blank=True)
    h_b5_strikes = models.IntegerField(null=True, blank=True)
    h_b5_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b5_put_outs = models.IntegerField(null=True, blank=True)
    h_b5_assists = models.IntegerField(null=True, blank=True)
    h_b5_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b6_at_bats = models.IntegerField(null=True, blank=True)
    h_b6_runs = models.IntegerField(null=True, blank=True)
    h_b6_hits = models.IntegerField(null=True, blank=True)
    h_b6_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b6_walks = models.IntegerField(null=True, blank=True)
    h_b6_strike_outs = models.IntegerField(null=True, blank=True)
    h_b6_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_pitches = models.IntegerField(null=True, blank=True)
    h_b6_strikes = models.IntegerField(null=True, blank=True)
    h_b6_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b6_put_outs = models.IntegerField(null=True, blank=True)
    h_b6_assists = models.IntegerField(null=True, blank=True)
    h_b6_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b7_at_bats = models.IntegerField(null=True, blank=True)
    h_b7_runs = models.IntegerField(null=True, blank=True)
    h_b7_hits = models.IntegerField(null=True, blank=True)
    h_b7_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b7_walks = models.IntegerField(null=True, blank=True)
    h_b7_strike_outs = models.IntegerField(null=True, blank=True)
    h_b7_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_pitches = models.IntegerField(null=True, blank=True)
    h_b7_strikes = models.IntegerField(null=True, blank=True)
    h_b7_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b7_put_outs = models.IntegerField(null=True, blank=True)
    h_b7_assists = models.IntegerField(null=True, blank=True)
    h_b7_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b8_at_bats = models.IntegerField(null=True, blank=True)
    h_b8_runs = models.IntegerField(null=True, blank=True)
    h_b8_hits = models.IntegerField(null=True, blank=True)
    h_b8_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b8_walks = models.IntegerField(null=True, blank=True)
    h_b8_strike_outs = models.IntegerField(null=True, blank=True)
    h_b8_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_pitches = models.IntegerField(null=True, blank=True)
    h_b8_strikes = models.IntegerField(null=True, blank=True)
    h_b8_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b8_put_outs = models.IntegerField(null=True, blank=True)
    h_b8_assists = models.IntegerField(null=True, blank=True)
    h_b8_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b9_at_bats = models.IntegerField(null=True, blank=True)
    h_b9_runs = models.IntegerField(null=True, blank=True)
    h_b9_hits = models.IntegerField(null=True, blank=True)
    h_b9_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b9_walks = models.IntegerField(null=True, blank=True)
    h_b9_strike_outs = models.IntegerField(null=True, blank=True)
    h_b9_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_pitches = models.IntegerField(null=True, blank=True)
    h_b9_strikes = models.IntegerField(null=True, blank=True)
    h_b9_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b9_put_outs = models.IntegerField(null=True, blank=True)
    h_b9_assists = models.IntegerField(null=True, blank=True)
    h_b9_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_b10_at_bats = models.IntegerField(null=True, blank=True)
    h_b10_runs = models.IntegerField(null=True, blank=True)
    h_b10_hits = models.IntegerField(null=True, blank=True)
    h_b10_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_b10_walks = models.IntegerField(null=True, blank=True)
    h_b10_strike_outs = models.IntegerField(null=True, blank=True)
    h_b10_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_pitches = models.IntegerField(null=True, blank=True)
    h_b10_strikes = models.IntegerField(null=True, blank=True)
    h_b10_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b10_put_outs = models.IntegerField(null=True, blank=True)
    h_b10_assists = models.IntegerField(null=True, blank=True)
    h_b10_hit_type = models.CharField(max_length=10, null=True, blank=True)

    h_at_bats = models.IntegerField(null=True, blank=True)
    h_runs = models.IntegerField(null=True, blank=True)
    h_hits = models.IntegerField(null=True, blank=True)
    h_runs_batted_in = models.IntegerField(null=True, blank=True)
    h_walks = models.IntegerField(null=True, blank=True)
    h_strike_outs = models.IntegerField(null=True, blank=True)
    h_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_b_pitches = models.IntegerField(null=True, blank=True)
    h_b_strikes = models.IntegerField(null=True, blank=True)
    h_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    h_put_outs = models.IntegerField(null=True, blank=True)
    h_assists = models.IntegerField(null=True, blank=True)
    h_hit_type = models.CharField(max_length=10, null=True, blank=True)
 
    v_b1_at_bats = models.IntegerField(null=True, blank=True)
    v_b1_runs = models.IntegerField(null=True, blank=True)
    v_b1_hits = models.IntegerField(null=True, blank=True)
    v_b1_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b1_walks = models.IntegerField(null=True, blank=True)
    v_b1_strike_outs = models.IntegerField(null=True, blank=True)
    v_b1_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_pitches = models.IntegerField(null=True, blank=True)
    v_b1_strikes = models.IntegerField(null=True, blank=True)
    v_b1_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b1_put_outs = models.IntegerField(null=True, blank=True)
    v_b1_assists = models.IntegerField(null=True, blank=True)
    v_b1_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b2_at_bats = models.IntegerField(null=True, blank=True)
    v_b2_runs = models.IntegerField(null=True, blank=True)
    v_b2_hits = models.IntegerField(null=True, blank=True)
    v_b2_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b2_walks = models.IntegerField(null=True, blank=True)
    v_b2_strike_outs = models.IntegerField(null=True, blank=True)
    v_b2_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_pitches = models.IntegerField(null=True, blank=True)
    v_b2_strikes = models.IntegerField(null=True, blank=True)
    v_b2_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b2_put_outs = models.IntegerField(null=True, blank=True)
    v_b2_assists = models.IntegerField(null=True, blank=True)
    v_b2_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b3_at_bats = models.IntegerField(null=True, blank=True)
    v_b3_runs = models.IntegerField(null=True, blank=True)
    v_b3_hits = models.IntegerField(null=True, blank=True)
    v_b3_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b3_walks = models.IntegerField(null=True, blank=True)
    v_b3_strike_outs = models.IntegerField(null=True, blank=True)
    v_b3_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_pitches = models.IntegerField(null=True, blank=True)
    v_b3_strikes = models.IntegerField(null=True, blank=True)
    v_b3_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b3_put_outs = models.IntegerField(null=True, blank=True)
    v_b3_assists = models.IntegerField(null=True, blank=True)
    v_b3_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b4_at_bats = models.IntegerField(null=True, blank=True)
    v_b4_runs = models.IntegerField(null=True, blank=True)
    v_b4_hits = models.IntegerField(null=True, blank=True)
    v_b4_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b4_walks = models.IntegerField(null=True, blank=True)
    v_b4_strike_outs = models.IntegerField(null=True, blank=True)
    v_b4_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_pitches = models.IntegerField(null=True, blank=True)
    v_b4_strikes = models.IntegerField(null=True, blank=True)
    v_b4_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b4_put_outs = models.IntegerField(null=True, blank=True)
    v_b4_assists = models.IntegerField(null=True, blank=True)
    v_b4_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b5_at_bats = models.IntegerField(null=True, blank=True)
    v_b5_runs = models.IntegerField(null=True, blank=True)
    v_b5_hits = models.IntegerField(null=True, blank=True)
    v_b5_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b5_walks = models.IntegerField(null=True, blank=True)
    v_b5_strike_outs = models.IntegerField(null=True, blank=True)
    v_b5_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_pitches = models.IntegerField(null=True, blank=True)
    v_b5_strikes = models.IntegerField(null=True, blank=True)
    v_b5_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b5_put_outs = models.IntegerField(null=True, blank=True)
    v_b5_assists = models.IntegerField(null=True, blank=True)
    v_b5_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b6_at_bats = models.IntegerField(null=True, blank=True)
    v_b6_runs = models.IntegerField(null=True, blank=True)
    v_b6_hits = models.IntegerField(null=True, blank=True)
    v_b6_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b6_walks = models.IntegerField(null=True, blank=True)
    v_b6_strike_outs = models.IntegerField(null=True, blank=True)
    v_b6_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_pitches = models.IntegerField(null=True, blank=True)
    v_b6_strikes = models.IntegerField(null=True, blank=True)
    v_b6_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b6_put_outs = models.IntegerField(null=True, blank=True)
    v_b6_assists = models.IntegerField(null=True, blank=True)
    v_b6_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b7_at_bats = models.IntegerField(null=True, blank=True)
    v_b7_runs = models.IntegerField(null=True, blank=True)
    v_b7_hits = models.IntegerField(null=True, blank=True)
    v_b7_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b7_walks = models.IntegerField(null=True, blank=True)
    v_b7_strike_outs = models.IntegerField(null=True, blank=True)
    v_b7_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_pitches = models.IntegerField(null=True, blank=True)
    v_b7_strikes = models.IntegerField(null=True, blank=True)
    v_b7_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b7_put_outs = models.IntegerField(null=True, blank=True)
    v_b7_assists = models.IntegerField(null=True, blank=True)
    v_b7_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b8_at_bats = models.IntegerField(null=True, blank=True)
    v_b8_runs = models.IntegerField(null=True, blank=True)
    v_b8_hits = models.IntegerField(null=True, blank=True)
    v_b8_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b8_walks = models.IntegerField(null=True, blank=True)
    v_b8_strike_outs = models.IntegerField(null=True, blank=True)
    v_b8_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_pitches = models.IntegerField(null=True, blank=True)
    v_b8_strikes = models.IntegerField(null=True, blank=True)
    v_b8_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b8_put_outs = models.IntegerField(null=True, blank=True)
    v_b8_assists = models.IntegerField(null=True, blank=True)
    v_b8_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b9_at_bats = models.IntegerField(null=True, blank=True)
    v_b9_runs = models.IntegerField(null=True, blank=True)
    v_b9_hits = models.IntegerField(null=True, blank=True)
    v_b9_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b9_walks = models.IntegerField(null=True, blank=True)
    v_b9_strike_outs = models.IntegerField(null=True, blank=True)
    v_b9_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_pitches = models.IntegerField(null=True, blank=True)
    v_b9_strikes = models.IntegerField(null=True, blank=True)
    v_b9_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b9_put_outs = models.IntegerField(null=True, blank=True)
    v_b9_assists = models.IntegerField(null=True, blank=True)
    v_b9_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_b10_at_bats = models.IntegerField(null=True, blank=True)
    v_b10_runs = models.IntegerField(null=True, blank=True)
    v_b10_hits = models.IntegerField(null=True, blank=True)
    v_b10_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_b10_walks = models.IntegerField(null=True, blank=True)
    v_b10_strike_outs = models.IntegerField(null=True, blank=True)
    v_b10_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_pitches = models.IntegerField(null=True, blank=True)
    v_b10_strikes = models.IntegerField(null=True, blank=True)
    v_b10_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b10_put_outs = models.IntegerField(null=True, blank=True)
    v_b10_assists = models.IntegerField(null=True, blank=True)
    v_b10_hit_type = models.CharField(max_length=10, null=True, blank=True)

    v_at_bats = models.IntegerField(null=True, blank=True)
    v_runs = models.IntegerField(null=True, blank=True)
    v_hits = models.IntegerField(null=True, blank=True)
    v_runs_batted_in = models.IntegerField(null=True, blank=True)
    v_walks = models.IntegerField(null=True, blank=True)
    v_strike_outs = models.IntegerField(null=True, blank=True)
    v_batting_average = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_on_base_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_on_base_plus_slugging = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_b_pitches = models.IntegerField(null=True, blank=True)
    v_b_strikes = models.IntegerField(null=True, blank=True)
    v_average_leverage_index = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_win_probability_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_win_probability_subtracted = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_base_out_runs_added = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    v_put_outs = models.IntegerField(null=True, blank=True)
    v_assists = models.IntegerField(null=True, blank=True)
    v_hit_type = models.CharField(max_length=10, null=True, blank=True)

class MLB_Game_link(models.Model):
    link = models.CharField(max_length=100)

# MLB Bets
class MLB_Scheduled_Game_Link(models.Model):
    links = models.TextField()
    
    def set_links(self, links_list):
        self.links = json.dumps(links_list)

    def get_links(self):
        return json.loads(self.links)

class MLB_Scheduled_Game(models.Model):
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

class MLB_Future(models.Model):
    #teams and odds are parallel arrays
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


class MLB_Special(models.Model):
    #bet_titles and odds are parallel arrays
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

class MLB_Player_Future(models.Model):
    #players and odds are parallel arrays
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
    
class MLB_Team_Playoff(models.Model):
    row_title = models.CharField(max_length=100)
    yes_odds = models.CharField(max_length=20, null=True, blank=True)
    no_odds = models.CharField(max_length=20, null=True, blank=True)

class MLB_Win_Total(models.Model):
    team = models.CharField(max_length=100)
    over_title = models.CharField(max_length=100)
    under_title = models.CharField(max_length=100)
    over_odds = models.CharField(max_length=20, null=True, blank=True)
    under_odds = models.CharField(max_length=20, null=True, blank=True)

class MLB_Game_Parlay(models.Model):
    #decimal_odds and #american_odds are parallel arrays
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

class MLB_Game_Prop(models.Model):
    #decimal_odds and #american_odds are parallel arrays
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

class MLB_GamePlayer_Prop(models.Model):
    #decimal_odds and #american_odds are parallel arrays
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

class MLB_Game_Special(models.Model):
    game_id = models.CharField(max_length=100, null=True, blank=True)
    game = models.CharField(max_length=100, null=True, blank=True)
    section_title = models.CharField(max_length=100)
    row_value = models.CharField(max_length=20, null=True, blank=True)
    odds = models.CharField(max_length=20, null=True, blank=True)

#NCAABB Bets

class NCAABB_Scheduled_Game(models.Model):
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

class NCAABB_Futures(models.Model):
    #teams and odds are parallel arrays
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

#NCAA FB Bets

class NCAAFB_Scheduled_Game(models.Model):
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

# NCAABasketBall Bets

class NCAABaskBall_Scheduled_Game(models.Model):
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

#NBA Bets

class NBA_Scheduled_Game(models.Model):
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

class NBA_Futures(models.Model):
    #teams and odds are parallel arrays
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

class NBA_Player_Futures(models.Model):
    # players and odds are parallel arrays
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
    
#WNBA Bets
    
class WNBA_Scheduled_Game(models.Model):
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

class WNBA_Futures(models.Model):
    # teams and odds are parallel arrays
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

class WNBA_Player_Futures(models.Model):
    # players and odds are parallel arrays
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

#MLS Bets

class MLS_Scheduled_Game(models.Model):
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

class MLS_Futures(models.Model):
    # teams and odds are parallel arrays 
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)