
## Temsah Python Library

Temsah is a powerful Python library specifically designed for web scraping e-commerce platforms such as Amazon. With its user-friendly interface and extensive functionality, Temsah allows developers to easily extract and collect product information and prices from these websites.Another usage has also been added to this library , Get the spot price of AED.

## Installation

You can install Temsah using pip:

```sh
pip install temsah
```

## Usage

Import Temsah at the beginning of your code:
```sh
import temsah
```

Then use the main function of the library to perform web scraping on the desired URL:
```sh
result = temsah.scrape(url)
```
It returns information from scraping e-commerce platforms.

Also in the new version of the library you can get the instant price of the dollar and the tangle with the following code:
```sh
object_currency = Currency()
data = object_currency.scrape()
print(data)
```
This code will show you an output similar to the output below:
```sh
{"AED_currency": "175,340" , "USD_currency" : "647,000"}
```

hope you enjoy !
## Supported Websites

Temsah provides support for the following e-commerce websites:
1. [Adidas](https://www.adidas.ae/)
2. [Nike](https://www.nike.ae/en/home)
3. [Amazon](https://www.amazon.ae/)
4. [Namshi](https://www.namshi.com/)
5. [Sharaf DG](https://uae.sharafdg.com/)
6. [Noon](https://www.noon.com/uae-en/)
7. [Carrefour](https://www.carrefouruae.com/)

## A website that is scraped to get instant prices
[tgju.org](https://www.tgju.org/profile/price_aed)
## Contact

For any inquiries or contributions to improving this library, please [contact me](mailto:seyedsahel1383@gmail.com "Email Me").

**Note**: This library is continuously being improved, and you are welcome to contribute to its enhancement.

