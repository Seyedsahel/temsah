from bs4 import BeautifulSoup
import requests
import chardet

#-------------------------------------
class Currency:
    def __init__(self):
    self.url_aed = 'https://www.tgju.org/profile/price_aed'
    self.url_dollar = 'https://www.tgju.org/profile/price_dollar_rl'
    self.currency = {}
#-------------------------------------

    def scrape(self):
        self.currency = {}
        self.scrape_aed()
        self.scrape_dollar()
        return self.currency

#-------------------------------------

    def scrape_aed(self):
        url = self.url_aed
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.5",
        }
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            encoding = chardet.detect(page.content)["encoding"]
            html = page.content.decode(encoding)
            soup = BeautifulSoup(html, "html.parser")
            scraper = self.get_aed(soup)
        else:
            print(f"page.status_code:{page.status_code}")

        return self.currency
            
    def get_aed(self, soup):
        
        self.currency = {}
      
        div_tag=soup.find('div',class_='fs-cell fs-xl-5 fs-lg-5 fs-md-12 fs-sm-12 fs-xs-12 top-header-item-block-1')
        if div_tag:
            div_tag=soup.find('div',class_='block-last-change-percentage')
            if div_tag:
                sp_tag = div_tag.find('span', class_='price')
                if sp_tag:
                    self.currency["AED_currency"] = sp_tag.text 
                else:
                    print('span tag not found')
            else:
                print('div tag not found')
        else:
            print('div tag not found')
            
    #--------------------scrape_dollar----------------------
    
    def scrape_dollar(self):
        url = self.url_dollar
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.5",
        }
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            encoding = chardet.detect(page.content)["encoding"]
            html = page.content.decode(encoding)
            soup = BeautifulSoup(html, "html.parser")
            self.get_dollar(soup)
        else:
            print(f"page.status_code:{page.status_code}")
    
    def get_dollar(self, soup):
    div_tag = soup.find('div', class_='fs-cell fs-xl-5 fs-lg-5 fs-md-12 fs-sm-12 fs-xs-12 top-header-item-block-1')
    if div_tag:
        div_tag = soup.find('div', class_='block-last-change-percentage')
        if div_tag:
            sp_tag = div_tag.find('span', class_='price')
            if sp_tag:
                self.currency["USD_currency"] = sp_tag.text 
            else:
                print('span tag not found for USD')
        else:
            print('div tag not found for USD')
    else:
        print('div tag not found for USD')

            