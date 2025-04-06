
from app.scraper.amazon_scraper import get_amazon_price
from app.scraper.flipkart_scraper import get_flipkart_price

def analyze_price(product_name):
    amazon_data = get_amazon_price(product_name)
    flipkart_data = get_flipkart_price(product_name)
    return [amazon_data, flipkart_data]
