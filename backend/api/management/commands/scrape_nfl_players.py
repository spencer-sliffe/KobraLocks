'''letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
            'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
positions = ['QB', 'RB', 'WR', 'TE', 'K']
teams = {"KC": ""}

for letter in letters:
    for position in positions:
        find td == position
            get href
            player link = f'https://www.footballdb.com/{href}'
            drive.get(player_link)
    driver.get(letter_link)

letter_link=f'https://www.footballdb.com/players/current.html?letter={letter}'


player_link_base = f'https://www.footballdb.com/'


class Command(BaseCommand):
    help = 'Scraping NFL players to put them into the player table'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def scrape_team_'''