# backend/api/management/command/scrape_mlb_game_links.py

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import json
from api.models import MLBGameLinks

class Command(BaseCommand):
    help = 'Scrape unique IDs from ESPNBet and store them in the MLBGameLinks model'

    def handle(self, *args, **kwargs):
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        MLBGameLinks.objects.all().delete()
        self.logger.info("Cleared the MLBGameLinks table in the database.")   
        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # URL to scrape
        url = "https://espnbet.com/sport/baseball/organization/united-states/competition/mlb"
        driver.get(url)
        time.sleep(10)  # Wait for the page to load

        # Parse page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all relevant divs and extract the unique part of the id
        divs = soup.find_all('div', class_='rounded p-4 bg-card-primary')
        unique_ids = []
        for div in divs:
            if 'id' in div.attrs:
                unique_id = div['id'].split('|')[1]
                unique_ids.append(unique_id)
                self.logger.info(f"Scraped unique ID: {unique_id}")

        driver.quit()

        # Save the unique IDs to the MLBGameLinks model
        self.save_links(unique_ids)
    
    def save_links(self, links_list):
        try:
            mlb_game_links = MLBGameLinks()
            mlb_game_links.set_links(links_list)
            mlb_game_links.save()
            self.logger.info("Saved links to MLBGameLinks model.")
        except Exception as e:
            self.logger.error(f"Error saving links to MLBGameLinks model: {str(e)}")



