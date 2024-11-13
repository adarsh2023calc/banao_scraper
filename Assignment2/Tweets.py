
from bs4 import BeautifulSoup
import csv

class Scraper:

    def __init__(self):
        self.headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
      }
        self.product_data=[]

        pass

    def scrap(self,csv_file):
        urls = self.get_links(csv_file)
        

    def get_links(self,csv_file):
        with open(csv_file,"r") as file:
            reader= csv.reader(file)
            links=[]
            for link in reader:
                links.append(link)
        return links
            
