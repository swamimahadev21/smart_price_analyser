from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_amazon_price(product_name):
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    query = product_name.replace(" ", "+")
    url = f"https://www.amazon.in/s?k={query}"
    driver.get(url)

    time.sleep(3)  # Wait for JS to load content

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    try:
        result = soup.select_one("div.s-main-slot div.s-result-item")
        title = result.select_one("h2 span")
        price = result.select_one(".a-price-whole")

        return {
            "site": "Amazon",
            "title": title.get_text(strip=True) if title else "Title not found",
            "price": "₹" + price.get_text(strip=True) if price else "Price not found"
        }
    except Exception as e:
        print("Error during scraping:", e)
        return {"site": "Amazon", "title": "Not found", "price": "N/A"}

# Test run
if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "iPhone 13"
    result = get_amazon_price(query)
    print("Amazon Result:", result["title"], "-", result["price"])
