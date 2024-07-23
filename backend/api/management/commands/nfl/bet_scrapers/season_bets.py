# backend/api/management/commands/scrape_nfl_division_specials.py
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from api.models import Available_Bet, League
import logging
import json

class Command(BaseCommand):
    help = 'Scrape NFL specials data from ESPNBet'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Clear the existing NFL Specials in the database
        self.logger.info("Scraping Available NFL Bets")
        link = "https://espnbet.com/sport/football/organization/united-states/competition/nfl"

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(link)
        time.sleep(2)  # Wait for the page to load
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.get_page_links(link, soup, options)
        driver.quit()

    def get_page_links(self, link, soup, options):
        self.logger.info(f"Getting page links for {link}")
        page_links = []
        link_buttons = soup.find('div', class_='no-scrollbar flex overflow-scroll m-0 w-full').find_all('button').text.strip()

        for link_button in link_buttons:
            link_button.lower()
            link_button.replace(' ', '-')
            page_links.append(link_button)

        self.get_nfl_pages(page_links, options)
    
    def get_page_html(self, driver, link):
        driver.get(link)
        time.sleep(2)  # Wait for the page to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.logger.info(f"Found html: {soup}")
        return soup

    def get_nfl_pages(self, page_links, options):
        self.logger.info(f"Getting html for pages {page_links}")
        htmls = []
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        for page_link in page_links:
            link = f"https://espnbet.com/sport/football/organization/united-states/competition/nfl/section/{page_link}"
            html = self.get_page_html(driver, link)
            htmls.append(html)
        driver.quit()
        self.scrape_nfl_season(htmls)

    def scrape_nfl_season(self, pages):
        self.logger.info(f"Scraping NFL Season Bets")
        for page in pages:
            self.handle_bet_page(page, 'NFL')
   
    def handle_bet_page(self, page, league):
        self.logger.info(f"handling bet pages")
        bet_sections = page.find_all('details', class_='group overflow-hidden rounded bg-card-primary-temp')
        for bet_section in bet_sections:
            self.handle_bet_section(bet_section, league)
    
    def handle_bet_section(self, bet_section, league):
        self.logger.info(f"handling bet sections")
        bet_description = bet_section.find('summary').find('h2', class_='text-style-m-medium flex-1').text.strip()
        rows_section = bet_section.find('div', class_='px-4 pb-4').find('div', class_='bg-card-primary-temp')
        rows = rows_section.find_all('div', class_='flex p-0')
        self.handle_bet_rows(rows, bet_description, league)
    
    def handle_bet_rows(self, rows, bet_description, league):

    
        
    def handle_player_future(self, player_future)
    
    
    def handle_future(self, future)
    
    def handle_total(self, total)
        
    def handle_spread(self, spread)

    def handle_special(self, special):
        try:
            section = special.find('h2', class_='text-style-m-medium flex-1')
            bet_title = section.text.strip()

            for allteam in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                team = allteam.find('span', class_='font-medium text-selector-label-deselected')
                team_text = team.text.strip()
                allteams.append(team_text)
            for allbettitle in special.find_all('button', class_='flex w-full items-center justify-between pr-4 pt-2 text-left cursor-default'):
                bet = allbettitle.find('div', class_='text-style-s-medium text-primary text-primary')
                bet_title = bet.text.strip()
                allbettitles.append(bet_title)
            for allodd in special.find_all('button', class_='relative rounded flex h-[48px] flex-1 flex-col items-center justify-center p-1.5 text-style-xs-medium button-bet-selector-deselected'):
                odd_detail = allodd.find('span', class_='font-bold')
                odd = odd_detail.text.strip()
                allodds.append(odd)

           
                LYID = 
                bet_titles=json.dumps(allbettitles),  # Encode list as JSON string
                team_titles=json.dumps(allteams),   # Encode list as JSON string
                odds=json.dumps(allodds)    # Encode list as JSON string
            )
            self.logger.info(f"Special saved: {section_title}")
        except Exception as e:
            self.logger.error(f"Error processing special: {str(e)}")
        
    def create_available_bet(self, bet):
        Available_Bet.objects.create(bet)
