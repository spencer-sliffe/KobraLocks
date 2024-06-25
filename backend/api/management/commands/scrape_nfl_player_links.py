from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import json
from api.models import NFL_player_link

class Command(BaseCommand):
    help = 'Scrape urls from football db'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        teams = [ '/nfl/team/roster/_/name/buf/buffalo-bills', '/nfl/team/roster/_/name/mia/miami-dolphins',
                 '/nfl/team/roster/_/name/ne/new-england-patriots', '/nfl/team/roster/_/name/nyj/new-york-jets', 
                '/nfl/team/roster/_/name/dal/dallas-cowboys', '/nfl/team/roster/_/name/phi/philadelphia-eagles', 
                '/nfl/team/roster/_/name/wsh/washington-commanders', '/nfl/team/roster/_/name/nyg/new-york-giants', 
                '/nfl/team/roster/_/name/den/denver-broncos', '/nfl/team/roster/_/name/kc/kansas-city-chiefs', 
                '/nfl/team/roster/_/name/lv/las-vegas-raiders', '/nfl/team/roster/_/name/lac/los-angeles-chargers', 
                '/nfl/team/roster/_/name/ari/arizona-cardinals', '/nfl/team/roster/_/name/lar/los-angeles-rams', 
                '/nfl/team/roster/_/name/sf/san-francisco-49ers', '/nfl/team/roster/_/name/sea/seattle-seahawks', 
                '/nfl/team/roster/_/name/bal/baltimore-ravens', '/nfl/team/roster/_/name/cin/cincinnati-bengals', 
                '/nfl/team/roster/_/name/cle/cleveland-browns', '/nfl/team/roster/_/name/pit/pittsburgh-steelers', 
                '/nfl/team/roster/_/name/chi/chicago-bears', '/nfl/team/roster/_/name/det/detroit-lions', 
                '/nfl/team/roster/_/name/gb/green-bay-packers', '/nfl/team/roster/_/name/min/minnesota-vikings', 
                '/nfl/team/roster/_/name/hou/houston-texans', '/nfl/team/roster/_/name/ind/indianapolis-colts',
                '/nfl/team/roster/_/name/jax/jacksonville-jaguars', '/nfl/team/roster/_/name/ten/tennessee-titans',
                '/nfl/team/roster/_/name/atl/atlanta-falcons', '/nfl/team/roster/_/name/car/carolina-panthers',
                '/nfl/team/roster/_/name/no/new-orleans-saints', '/nfl/team/roster/_/name/tb/tampa-bay-buccaneers']
        
        
        # URL to scrape
        for team in teams:
            url = f"https://www.espn.com{team}"
            driver.get(url)
            time.sleep(10)  # Wait for the page to load
            self.logger.info(f"Connected to link: {url}")
            # Parse page content
            soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all relevant divs and extract the unique part of the id
            section = soup.find('tbody', class_='Table__TBODY')
            rows = section.find_all('tr', class_='Table__TR Table__TR--lg Table__even')
            for row in rows:
                columns = row.find_all('td', class_='Table__TD')
                position = columns[2].text.strip()
                self.logger.info(f"{position}")
                if position not in ['QB', 'RB', 'WR', 'TE', 'K']:
                    self.logger.info("Not right position coninuing to next")
                    continue
                else:
                    link_column = columns[1].find('a')
                    og_link = link_column['href']
                    self.logger.info(f"found link: {og_link}")
                    # Split the URL into parts
                    link_parts = og_link.split('/')

                    # Insert 'stats' into the appropriate position
                    link_parts.insert(6, 'stats')

                    # Join the parts back together into a single URL
                    link = '/'.join(link_parts)
                    self.save_link(link)
    # Your code here
        driver.quit()        
    
    def save_link(self, link):
        try:
            NFL_player_link.objects.create(
                link = link
            )
            self.logger.info(f"Saved link: {link}")
        except Exception as e:
            self.logger.error(f"Error saving link: {e}")



