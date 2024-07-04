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




# Players




# Games

class MLB_Game(models.Model):
    GID = models.CharField(max_length=10, primary_key=True)  # Universal game ID
    LYID = models.ForeignKey(League, on_delete=models.CASCADE)  # League Year ID as a foreign key
    Date = models.DateField()
    h_TYID = models.ForeignKey(MLB_Team, related_name='home_games', on_delete=models.CASCADE)  # Home team's team ID
    v_TYID = models.ForeignKey(MLB_Team, related_name='away_games', on_delete=models.CASCADE)  # Visiting team's team ID

    def __str__(self):
        return f"Game {self.GID} on {self.Date}"


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


class MLBSpecials(models.Model):
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

class MLBPlayerFutures(models.Model):
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

class MLBGameProps(models.Model):
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

class MLBGamePlayerProps(models.Model):
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

class NFLPlayerFutures(models.Model):
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

class NFLPlayerTotals(models.Model):
    row_title = models.CharField(max_length=100)
    over_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    under_decimal_odds = models.CharField(max_length=20, null=True, blank=True)
    over_american_odds = models.CharField(max_length=20, null=True, blank=True)
    under_american_odds = models.CharField(max_length=20, null=True, blank=True)

class NFLDivisionSpecials(models.Model):
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

class NFLSeasonSpecials(models.Model):
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

class NBAPlayerFutures(models.Model):
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

class WNBAPlayerFutures(models.Model):
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

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)