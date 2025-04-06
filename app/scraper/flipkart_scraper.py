
import requests
from bs4 import BeautifulSoup

def get_flipkart_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    query = product_name.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    try:
        title = soup.select_one("div._4rR01T").get_text(strip=True)
        price = soup.select_one("div._30jeq3").get_text(strip=True)
        return {"site": "Flipkart", "title": title, "price": price}
    except:
        return {"site": "Flipkart", "title": "Not found", "price": "N/A"}
