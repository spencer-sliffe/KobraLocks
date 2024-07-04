# api/management/commands/scrape_all_mlb_game_bets.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from concurrent.futures import ThreadPoolExecutor, as_completed

class Command(BaseCommand):
    help = 'Run all of mlb games bet scrape commands concurrently'

    def handle(self, *args, **kwargs):
        # First, run scrape_mlb_game_links command
        self.stdout.write("Starting scrape_mlb_game_links...\n")
        call_command('scrape_mlb_game_links')
        self.stdout.write("Finished scrape_mlb_game_links.\n")

        # Commands to run concurrently
        commands = [
            'scrape_mlb_games',
            'scrape_mlb_game_parlays',
            'scrape_mlb_game_props',
            'scrape_mlb_player_props',
            'scrape_mlb_game_specials',
            'scrape_mlb_futures',
            'scrape_mlb_player_futures',
            'scrape_mlb_playoffs',
            'scrape_mlb_specials',
            'scrape_mlb_wins',
            'scrape_mlb_specials',
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

        self.stdout.write("All commands executed successfully.\n")

