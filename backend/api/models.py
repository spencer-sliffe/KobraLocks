from django.db import models
from django.contrib.auth.models import User

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


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)