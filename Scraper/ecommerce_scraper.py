import requests
from bs4 import BeautifulSoup


class scraper():

    def __init__(self, url):
        self.url = url
        

    def scrape(self):
        # Get the HTML of the page
        r = requests.get(self.url)
        # Create a BeautifulSoup object
        soup = BeautifulSoup(r.text, 'html.parser')
        # Get the product name
        name = soup.find('h1', class_='product-name').text.strip()
        # Get the product price
        price = soup.find('span', class_='price').text.strip()
        # Get the product image
        image = soup.find('img', class_='product-image-photo')['src']
        # Get the product description
        description = soup.find('div', class_='product attribute description').text.strip()
        # Get the product rating
        rating = soup.find('span', class_='rating').text.strip()
        # Get the product reviews
        reviews = soup.find('div', class_='product-reviews-summary').text.strip()
        # Get the product availability
        availability = soup.find('p', class_='availability in-stock').text.strip()
        # Get the product SKU
        sku = soup.find('span', class_='value').text.strip()
        # Get the product brand
        brand = soup.find('a', class_='brand').text.strip()
        # Get the product category
        category = soup.find('a', class_='category').text.strip()
        # Get the product subcategory
        subcategory = soup.find('a', class_='subcategory').text.strip()
        # Get the product tags
        tags = soup.find('div', class_='product-tags').text.strip()
        # Get the product URL
        url = self.url
        # Create a dictionary of the product information
        product = {
            'name': name,
            'price': price,
            'image': image,
            'description': description,
            'rating': rating,
            'reviews': reviews,
            'availability': availability,
            'sku': sku,
            'brand': brand,
            'category': category,
            'subcategory': subcategory,
            'tags': tags,
            'url': url
        }
        # Return the product dictionary
        return product