import requests
from bs4 import BeautifulSoup
import chardet
from .data_extractor import *


# ---------------------------

class Temsah:

    def __init__(self, url):
        self.url = url

    def scrape(self):
        url = self.url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.5",
        }
        page = requests.get(url, headers=headers)
        # print(page.text)
        if page.status_code == 200:
            encoding = chardet.detect(page.content)["encoding"]
            html = page.content.decode(encoding)
            soup = BeautifulSoup(html, "html.parser")
            scraper = Extractor(soup)
            # ---------------------------

            site_name = url[12:]
            if site_name.startswith("amazon"):
                scraper.amazon()
            elif site_name.startswith("nike"):
                scraper.nike()
            elif site_name.startswith("adidas"):
                scraper.adidas()
            elif site_name.startswith("namshi"):
                scraper.namshi()
            elif "sharafdg" in site_name:
                scraper.sharafdg()
            elif site_name.startswith("noon"):
                scraper.noon()
            elif site_name.startswith("carrefouruae"):
                scraper.carre()

            scraper.product.url = url

            return scraper.product

        else:
            print(f"page.status_code:{page.status_code}")
