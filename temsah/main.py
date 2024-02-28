import requests
from bs4 import BeautifulSoup
import chardet


#You can use the commented codes to test the code
#---------------------------
class Product:
    def __init__(self,site):
        self.name = ""
        self.site = site
        self.price = ""
        self.discount = False
        self.price_out = ""
        self.price_in = ""
        self.image = ""
        self.url = ""

    def __str__(self):
        output = f"name: {self.name}\nsite: {self.site}\n"
        if(not self.discount):
            output += f"price: {self.price}\n"
        output += f"discount: {self.discount}\nprice_out: {self.price_out}\nprice_in: {self.price_in}\nimage: {self.image}\nurl: {self.url}"
        return output
#---------------------------
class find :
    def __init__(self,soup):
        self.soup = soup 
        self.product = None
        
    def amazon(self):
        soup = self.soup
        self.product = Product("amazon")
        
        try:  
                #product name
                title=soup.find('title')
                if title:
                    product_name=title.text[12:]
                    self.product.name = product_name.strip()
                    # print(f"product name:{product_name}") 
                else:
                    print('product name tag not found')
                
                #img
                div_tag = soup.find('div', id='imgTagWrapperId', class_='imgTagWrapper')
                if div_tag:
                    img_tag = div_tag.find('img')
                    if img_tag:
                        self.product.image = img_tag['src']
                        # print(f"img src:{img_tag['src']}")  #img src
                else:
                    print('img tag not found')

                #price  
                span_tag = soup.find('span', class_='a-price a-text-price')
                if span_tag:
                    price_out=span_tag.find('span' , class_='a-offscreen')
                    if price_out: #in discount

                        self.product.price_out = price_out.text.strip()
                        self.product.discount = True
                
                        price_in = soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
                        if price_in:
                            # self.product.price_in = price_in.text.strip()
                            self.product.price_in = price_in.text.strip()
                        else:
                            print('price not found')  
                else:
                    price = soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
                    if price:
                        # self.product.price = price.text.strip()
                        # self.product.discount = False
                        self.product.price = price.text.strip()
                        self.product.discount = False
                    else:
                        print('price not found')

        except Exception as e:
            print(f"An error occurred while scraping the URL amazon")
            print(e)
        
    
    #---------------------------

    def nike(self):
        soup=self.soup
        self.product = Product("nike")
        
        try:

            #product name
            name=soup.find('span',class_='b-pdp__product-name js-gtm-product-name')
            if name:
                product_name=name.text
                self.product.name = product_name.strip()
                    
            else:
                print('product name tag not found')
            
            #img
            img_tag = soup.find('img', class_='b-picture__img b-pdpimages__carousel-img js-zoomed-img js-lazy-disabled')
            if img_tag:
                self.product.image = img_tag['src']
            else:
                print('img tag not found')

            #price

            span=soup.find('span', class_="strike-through list")  
            if span: #discount
                self.product.discount = True
                sp=span.find('span',class_='value')
                self.product.price_out = sp['content'].strip()
            span_tag = soup.find('span', class_='sales')
            if span_tag:
                sp=span_tag.find('span',class_='value')
                if self.product.discount:
                    self.product.price_in = sp.text.strip()
                else:
                    self.product.price = sp.text.strip()

            else:
                print('price tag not found')
                        
                
        except Exception as e:
                    print(f"An error occurred while scraping the URL nike")
                    print(e)

    #---------------------------

    def adidas(self):
        soup=self.soup
        self.product = Product("adidas")
        
        try:
            
            #product name
            name=soup.find('h1',class_='product-name')
            if name:
                product_name=name.text
                self.product.name = product_name.strip()
            else:
                print('product name tag not found')

            #img
            div_tag= soup.find('div',class_='main_image sub_img')
            if div_tag:
                img_tag = div_tag.find('img', class_='img-fluid')
                if img_tag:
                    self.product.image = img_tag['src']
                else:
                    print('img tag not found')
            else:
                        print('img tag not found')

            #price
            div_tag = soup.find('div', class_='price')
            if div_tag:
                span_tag=div_tag.find('span',class_='sales')
                if span_tag:
                    price_in=span_tag.find('span',class_='value')
                    price_out=div_tag.find('span',class_='value')
                    if price_in['content'] == price_out['content'] : 
                        self.product.price = price_in
                        self.product.discount = False
                    else:
                        self.product.price_out = price_out
                        self.product.price_in = price_in
                        self.product.discount = True
            else:
                print('price tag not found')

        
        except Exception as e:
            print(f"An error occurred while scraping the URL adidas")
            print(e)

    #---------------------------

    def namshi(self):
        soup = self.soup
        self.product = Product("namshi")
        
        try:
            #product name
            name = soup.find('h1',class_='ProductConversion_productTitle__dvlc5')
            if name:
                product_name = name.text
                self.product.name = product_name.strip()
            else:
                print('name tag not found')

            #img
            div_tag = soup.find('div', class_='ImageGallery_imageContainer__jmn93')
            final_src = ""
            if div_tag:
                img_tag = div_tag.find('img')
                if img_tag:
                    final_src = f"https://www.namshi.com{img_tag['src']}"
                    self.product.image = final_src
            else:
                print('img tag not found')

            #price
            span1_tag = soup.find('span', class_='ProductPrice_sellingPrice__y8kib ProductPrice_xLarge__6DRdu')
            if span1_tag:
                span2_tag = span1_tag.find('span', class_='ProductPrice_value__hnFSS')
                self.product.discount = False
                self.product.price = span2_tag.text
            else:
                self.product.discount = True
                div_tag=soup.find('div',class_='ProductPrice_preReductionPrice__S72wT') #in discount
                if div_tag:
                    self.product.price_out = div_tag.text
                else:
                    print('price tag not found')
                span_tag=soup.find('span',class_='ProductPrice_sellingPrice__y8kib ProductPrice_discounted__Puxu6 ProductPrice_xLarge__6DRdu')
                if span_tag:
                    self.product.price_in = span_tag.text
                else:
                    print('price tag not found')

        except Exception as e:
            print(f"An error occurred while scraping the URL namshi")
            print(e)


    #---------------------------

           
    def sharafdg(self):
        soup = self.soup
        self.product = Product("sharafdg")

        #product name 
        try:
            name=soup.find('h1',class_='product_title entry-title')
            if name:
                product_name=name.text
                self.product.name = product_name.strip() 
            else:
                print('name tag not found')
            
            #img
            img_tag = soup.find('img', class_='img-responsive elevateZoom')
            if img_tag:
                self.product.image = img_tag['src'] #img src
            else:
                print('img tag not found')

            #price 
                
            self.product.discount = False
            div_tag = soup.find('span', class_='strike')
            if div_tag:
                self.product.discount = True
                self.product.price_out = div_tag.text.strip()
            
            div_tag = soup.find('div', class_='price')
            if div_tag:
                span_tag = div_tag.find('span', class_='total--sale-price')
                if span_tag :
                    if self.product.discount:
                        self.product.price_out = span_tag.text.strip()
                    else:
                        self.product.price = span_tag.text.strip()
                        
                else:
                    print('price tag not found')
        

        except Exception as e:
            print(f"An error occurred while scraping the URL sharafdg")
            print(e)

    #---------------------------
    def noon(self):
        soup=self.soup
        self.product = Product("noon")
        try:
            #product name  
            name=soup.find('h1',class_='sc-f5f69516-18 cmxvfi')
            if name:
                product_name=name.text
                self.product.name = product_name.strip() 
            else:
                print('name tag not found')

            #img 
            div_tag = soup.find('div', class_='sc-d8caf424-2 fJBKzl')
            if div_tag:
                img_tag = div_tag.find('img')
                if img_tag:
                    self.product.image = img_tag['src']
            else:
                print('img tag not found')

            #price
            div_tag = soup.find('div', class_='sc-4de52a49-0 deGxov')
            if div_tag:
                price_out = div_tag.find('div', class_='priceWas')
                price_in= div_tag.find('div',class_='priceNow')
                if price_out: #discount
                    self.product.discount = True
                    self.product.price_out = price_out.text
                    self.product.price_in = price_in.text
                else:
                    self.product.price = price_in.text
                    self.product.discount = False
            else:
                print("price tag not found")

        except Exception as e:
            print(f"An error occurred while scraping the URL")
            print(e)

    #---------------------------

    def carre(self):
        soup = self.soup
        self.product = Product("carre")
        try:
            #product name
            name=soup.find('h1',class_='css-106scfp')
            if name:
                product_name=name.text
                self.product.name = product_name.strip() 
            else:
                print('name tag not found')

            #img  
            div_tag = soup.find('div', class_='css-1d0skzn')
            if div_tag:
                img_tag = div_tag.find('img')
                if img_tag:
                    self.product.image = img_tag['src']
            else:
                print('img tag not found')

            #price    
            div_tag = soup.find('div', class_='css-1oh8fze')
            if div_tag:
                price_out = div_tag.find('span', class_='css-rmycza')
                if price_out:
                    self.product.price_out = price_out.text
                    self.product.discount = True
                    price_in= div_tag.find('h2',class_='css-1i90gmp')
                    input_string = price_in.text
                    start_index = input_string.find("AED ")  
                    end_index = input_string.find("AED ", start_index + 1)  
                    if start_index != -1 and end_index != -1:
                        modified_string = input_string[start_index:end_index]
                        self.product.price_in = modified_string  
                    else:
                        print("AED not found in the input string")   
                else:
                    price = div_tag.find('h2', class_='css-17ctnp')
                    if price:
                        self.product.price = price.text
                        self.product.discount = False
            else:
                print('price tag not found')

        except Exception as e:
            print(f"An error occurred while scraping the URL")
            print(e)
    
#---------------------------

class main :
    
    def __init__(self,url):
        self.url = url
    
    def scrape(self):
        url = self.url
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.5',
        }
        page=requests.get(url,headers=headers)
        # print(page.text)
        if page.status_code == 200:
            encoding = chardet.detect(page.content)["encoding"]
            html = page.content.decode(encoding)
            soup = BeautifulSoup(html, 'html.parser') 
            scraper = find(soup)
    #---------------------------

            site_name = url[12:]
            if site_name.startswith('amazon'):
                scraper.amazon()   
            elif site_name.startswith('nike'):
                scraper.nike()
            elif site_name.startswith('adidas'):
                scraper.adidas()
            elif site_name.startswith('namshi'):
                scraper.namshi()
            elif "sharafdg" in site_name:
                scraper.sharafdg()
            elif site_name.startswith('noon'):
                scraper.noon()
            elif site_name.startswith('carrefouruae'):
                scraper.carre()
                

            scraper.product.url = url
                
            return scraper.product

        else:
            print(f"page.status_code:{page.status_code}")

