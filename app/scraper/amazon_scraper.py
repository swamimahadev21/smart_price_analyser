
import requests
from bs4 import BeautifulSoup

def get_amazon_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    query = product_name.replace(" ", "+")
    url = f"https://www.amazon.in/s?k={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    try:
        title = soup.select_one("span.a-text-normal").get_text(strip=True)
        price = soup.select_one("span.a-price-whole").get_text(strip=True)
        return {"site": "Amazon", "title": title, "price": price}
    except:
        return {"site": "Amazon", "title": "Not found", "price": "N/A"}
