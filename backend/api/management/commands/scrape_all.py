# api/management/commands/scrape_all.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from concurrent.futures import ThreadPoolExecutor, as_completed

class Command(BaseCommand):
    help = 'Run all scrape commands concurrently'

    def handle(self, *args, **kwargs):
        commands = [
            'scrape_mlb_futures',
            'scrape_mlb_games',
            'scrape_mlb_player_futures',
            'scrape_mlb_playoffs',
            'scrape_mlb_specials',
            'scrape_mlb_wins',
            'scrape_mlb_games',
            'scrape_mls_futures',
            'scrape_nba_futures',
            'scrape_nba_games',
            'scrape_nba_player_futures',
            'scrape_ncaabb_futures',
            'scrape_ncaabb_games',
            'scrape_ncaafb_games',
            'scrape_nfl_division_specials',
            'scrape_nfl_futures',
            'scrape_nfl_games',
            'scrape_nfl_player_futures',
            'scrape_nfl_player_totals',
            'scrape_nfl_season_specials',
            'scrape_wnba_futures',
            'scrape_wnba_games',
            'scrape_wnba_player_futures'
        ]

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_command = {executor.submit(call_command, command): command for command in commands}

            for future in as_completed(future_to_command):
                command = future_to_command[future]
                try:
                    future.result()
                    self.stdout.write(f"Finished {command}.\n")
                except Exception as exc:
                    self.stderr.write(f"{command} generated an exception: {exc}\n")

        self.stdout.write("All commands executed successfully.")
