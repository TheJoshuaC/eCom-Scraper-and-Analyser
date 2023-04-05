import csv

from analysis import DataCleanser, DataVisualiser
from scraper import EcommerceScraper, Parser

# Define the product URLs you want to scrape
product_urls = [
    'https://www.beserk.com.au/products/m-wall083c-s5-platform-boots-in-stock?variant=40119850467462,',
    # Add more product URLs here
]

# Define the output CSV file path
output_file = 'data/raw_data.csv'

# Write the header row for the CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'price', 'image', 'description', 'rating', 'reviews', 'availability', 'sku', 'brand', 'category', 'subcategory', 'tags', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Iterate through the product URLs and scrape data
for url in product_urls:
    scraper = EcommerceScraper(url)
    html_content = scraper.scrape()
    
    if html_content is not None:
        parser = Parser(html_content)
        product_data = parser.parse_product_data()

        # Write the product data to the CSV file
        with open(output_file, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(product_data)
    else:
        print(f"Failed to scrape data from: {url}")

print("Data scraping completed.")