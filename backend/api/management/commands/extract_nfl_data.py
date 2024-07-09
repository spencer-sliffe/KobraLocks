# api/management/commands/extract_nfl_data.py
import pandas as pd
from django.core.management.base import BaseCommand
from api.models import NFL_Team, NFL_Player, NFL_Division, NFL_Game,

class Command(BaseCommand):
    help = 'Extract NFL team data from the database'

    def handle(self, *args, **kwargs):
        teams = NFL_Team.objects.all().values()
        players = NFL_Player.objects.all().values()
        divisions = NFL_Player.objects.all().values()
        games = NFL_Player.objects.all().values()
        

        df_1 = pd.DataFrame(list(teams))
        df_2 = pd.DataFrame(list(players))
        df_3 = pd.DataFrame(list(divisions))
        df_4 = pd.DataFrame(list(games))

        df_1.to_csv('nfl_team_data.csv', index=False)
        df_2.to_csv('nfl_player_data.csv', index=False)
        df_3.to_csv('nfl_division_data.csv', index=False)
        df_4.to_csv('nfl_game_data.csv', index=False)
        self.stdout.write(self.style.SUCCESS('Successfully extracted NFL team, player, division, and game data'))
