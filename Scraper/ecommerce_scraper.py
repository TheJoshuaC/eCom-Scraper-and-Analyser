import requests
from bs4 import BeautifulSoup


class EcommerceScraper:

    def __init__(self, url):
        """Initialize the scraper with a URL of the product page."""
        self.url = url 
        self.session = requests.Session()

    def url_check(self):
        """Check if the URL is valid."""
        try:
            r = self.session.get(self.url)
            r.raise_for_status()
            return True
        except:
            return False

    def scrape(self):
        """Scrape the product data from the given URL."""
        if not self.url_check():
            return None

        r = self.session.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        def find_element(soup_obj, element, class_name, attr=None):
            """Find an element in the soup object and return its attribute or text."""
            result = soup_obj.find(element, class_=class_name)
            return result[attr].strip() if result and attr else result.text.strip() if result else None

        product = {
            'name': find_element(soup, 'h1', 'product-name'),
            'price': find_element(soup, 'span', 'price'),
            'image': find_element(soup, 'img', 'product-image-photo', 'src'),
            'description': find_element(soup, 'div', 'product attribute description'),
            'rating': find_element(soup, 'span', 'rating'),
            'reviews': find_element(soup, 'div', 'product-reviews-summary'),
            'availability': find_element(soup, 'p', 'availability in-stock'),
            'sku': find_element(soup, 'span', 'value'),
            'brand': find_element(soup, 'a', 'brand'),
            'category': find_element(soup, 'a', 'category'),
            'subcategory': find_element(soup, 'a', 'subcategory'),
            'tags': find_element(soup, 'div', 'product-tags'),
            'url': self.url
        }

        return product