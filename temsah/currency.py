from bs4 import BeautifulSoup
import requests
import chardet
# ---------------------------
class Currency:
    def __init__(self):
        self.url = 'https://www.tgju.org/profile/price_aed'
        self.currency = {}


    
    def scrape(self):
        url = self.url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.5",
        }
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            encoding = chardet.detect(page.content)["encoding"]
            html = page.content.decode(encoding)
            soup = BeautifulSoup(html, "html.parser")
            scraper = self.get(soup)
            # ---------------------------
        else:
            print(f"page.status_code:{page.status_code}")

        return self.currency
            
    def get(self, soup):
        
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
            