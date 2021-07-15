from bs4 import BeautifulSoup
import requests
import html5lib
from lxml import etree
import lxml

EMAIL = "shampadsh@gmail.com"
PASSWORD = "5946644S"

URL = "https://www.amazon.com/Casio-Womens-LRW200H-7BVCF-Sport-Watch/dp/B00791QYMQ"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

title = soup.find("span", id="productTitle").getText().strip()
print(title)

price = soup.xpath('//*[@id="priceblock_ourprice"]')

print(price)





