import requests
import csv
import numpy as np
from bs4 import BeautifulSoup



class Scraper:

    def __init__(self):
        self.headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
      }
        self.product_data=[]
        pass

    def scrap(self,url):
        
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            page_content = response.content
            soup = BeautifulSoup(page_content, 'html.parser')
            products = soup.find_all('div',"a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
            for product in products:
                product_data = {
                    "name": self.scrap_product_name(product),
                    "ratings": self.scrap_ratings(product)[:3],
                    "no_of_reviews": self.scrap_no_of_reviews(product),
                    "current_price": self.scrap_current_price(product),
                    "original_price": self.scrap_original_price(product)
                }
                # Append the product data to the list
                self.product_data.append(product_data)
            
            self.product_data = np.array(self.product_data)
            np.savetxt('battery.csv', self.product_data, delimiter=",", fmt="%s",comments="")
            

        else:
            print("Failed to retrieve the webpage")

    def scrap_product_name(self,soup):
        
        name=soup.find("span",class_="a-size-base-plus a-color-base a-text-normal")
        return name.text
    
    def scrap_ratings(self,soup):
        
        names=soup.find("span",class_="a-icon-alt")
        return names.text
    
    def scrap_no_of_reviews(self,soup):
        
        reviews= soup.find("span",class_="a-size-base s-underline-text")
        return reviews.text
    
    def scrap_current_price(self,soup):
        price = soup.find("span",class_="a-price-whole")
        return price.text
    
    def scrap_original_price(self,soup):
        price_class = soup.find("span",class_="a-price a-text-price")
        price=price_class.find("span",class_="a-offscreen")
        return price.text


if __name__ =="__main__":
    url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'
    scraper = Scraper()
    scraper.scrap(url)

