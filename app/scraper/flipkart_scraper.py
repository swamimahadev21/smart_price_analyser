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
        title = soup.select_one("div._4rR01T")
        price = soup.select_one("div._30jeq3")
        
        return {
            "site": "Flipkart",
            "title": title.get_text(strip=True) if title else "Title not found",
            "price": price.get_text(strip=True) if price else "Price not found"
        }
    except Exception as e:
        print("Error during Flipkart scraping:", e)
        return {"site": "Flipkart", "title": "Not found", "price": "N/A"}

# ✅ CLI test support
if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "iPhone 13"
    result = get_flipkart_price(query)
    print("Flipkart Result:", result["title"], "-", result["price"])
