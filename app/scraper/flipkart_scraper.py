from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_flipkart_price(product_name):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    query = product_name.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={query}"
    driver.get(url)
    
    time.sleep(5)

    # Save the full page to inspect it
    with open("flipkart_output.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    soup = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()

    try:
        title = soup.select_one("div._4rR01T").get_text(strip=True)
        price = soup.select_one("div._30jeq3").get_text(strip=True)
        return {"site": "Flipkart", "title": title, "price": price}
    except:
        return {"site": "Flipkart", "title": "Not found", "price": "N/A"}

if __name__ == "__main__":
    result = get_flipkart_price("iPhone 13")
    print(f"Flipkart Result: {result['title']} - {result['price']}")
