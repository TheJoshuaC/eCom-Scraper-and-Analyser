# scraper/parser.py
from bs4 import BeautifulSoup

"""Parse the HTML content of a product page."""
class Parser:

    """Parse the HTML content of a product page."""
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    """Find an element in the soup object and return its attribute or text."""
    def find_element(self, element, class_name, attr=None):
        result = self.soup.find(element, class_=class_name)
        return result[attr].strip() if result and attr else result.text.strip() if result else None

    """Parse the product data from the soup object."""
    def parse_product_data(self):
        product = {
            'name': self.find_element('h1', 'product-name'),
            'price': self.find_element('span', 'price'),
            'image': self.find_element('img', 'product-image-photo', 'src'),
            'description': self.find_element('div', 'product attribute description'),
            'rating': self.find_element('span', 'rating'),
            'reviews': self.find_element('div', 'product-reviews-summary'),
            'availability': self.find_element('p', 'availability in-stock'),
            'sku': self.find_element('span', 'value'),
            'brand': self.find_element('a', 'brand'),
            'category': self.find_element('a', 'category'),
            'subcategory': self.find_element('a', 'subcategory'),
            'tags': self.find_element('div', 'product-tags'),
            'url': self.url
        }

        return product