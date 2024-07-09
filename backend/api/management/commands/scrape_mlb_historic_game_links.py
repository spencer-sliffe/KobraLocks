from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from api.models import MLB_Game_link
import time

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
        years = {"2024"}

        for year in years:     
            url = f"https://www.baseball-reference.com/leagues/majors/{year}-schedule.shtml"
            driver.get(url)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            self.scrape_links(soup)
            self.logger.info("connecting to new link")
        
    
    def scrape_links(self, soup):
        content = soup.find('div', class_='section_wrapper')
        section = content.find('div', class_='section_content')
        days = section.find_all('div')[7:]
        self.logger.info("found content, section, days")

        for day in days:
            games = day.find_all('p', class_='game')
            self.logger.info("found games")
            for game in games:
                boxscore_section = game.find('em')
                self.logger.info("found em")
                boxscore_href = boxscore_section.find('a')
                self.logger.info("found a")
                boxscore_link = boxscore_href['href']
                link = f"https://www.baseball-reference.com/{boxscore_link}"
                self.add_link(link)
    
    def add_link(self, link):
        try:
            MLB_Game_link.objects.create(
                link = link
            )
            self.logger.info(f"Saved link: {link}")
        except Exception as e:
            self.logger.error(f"Error saving link: {e}")

