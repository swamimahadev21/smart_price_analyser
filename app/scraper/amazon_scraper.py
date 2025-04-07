from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_amazon_price(product_name):
    options = Options()
    options.add_argument("--headless")  # Run without GUI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-blink-features=AutomationControlled')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    query = product_name.replace(" ", "+")
    url = f"https://www.amazon.in/s?k={query}"
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    try:
        results = soup.select("div.s-main-slot div[data-component-type='s-search-result']")
        for item in results:
            title_tag = item.select_one("h2 span")
            price_whole = item.select_one("span.a-price-whole")
            price_fraction = item.select_one("span.a-price-fraction")
            if title_tag and price_whole:
                title = title_tag.get_text(strip=True)
                price = f"₹{price_whole.get_text(strip=True)}.{price_fraction.get_text(strip=True) if price_fraction else '00'}"
                return {
                    "site": "Amazon",
                    "title": title,
                    "price": price
                }

        return {"site": "Amazon", "title": "Not found", "price": "N/A"}
    except Exception as e:
        print("Error during scraping:", e)
        return {"site": "Amazon", "title": "Not found", "price": "N/A"}

# Test run
if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "iPhone 13"
    result = get_amazon_price(query)
    print("Amazon Result:", result["title"], "-", result["price"])
