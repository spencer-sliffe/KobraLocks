from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    game_time = models.DateTimeField(null=True, blank=True)
    live = models.BooleanField(default=False)
    inning_state = models.CharField(max_length=100, null=True, blank=True)  # Combined field
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)
    balls = models.IntegerField(null=True, blank=True)
    strikes = models.IntegerField(null=True, blank=True)
    outs = models.IntegerField(null=True, blank=True)
    team1_spread = models.CharField(max_length=20, null=True, blank=True)
    team2_spread = models.CharField(max_length=20, null=True, blank=True)
    team1_total = models.CharField(max_length=20, null=True, blank=True)
    team2_total = models.CharField(max_length=20, null=True, blank=True)
    team1_money = models.CharField(max_length=20, null=True, blank=True)
    team2_money = models.CharField(max_length=20, null=True, blank=True)

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, blank=True, null=True)