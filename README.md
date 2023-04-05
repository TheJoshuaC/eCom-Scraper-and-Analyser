# eCom-Scraper-and-Analyser

Start of an eCommerce scraper, a request from a person close to me

EcommerceDataScraper/
│
├── scraper/
│   ├── __init__.py
│   ├── ecommerce_scraper.py
│   └── parser.py
│
├── analysis/
│   ├── __init__.py
│   ├── data_cleaner.py
│   └── visualizer.py
│
├── data/
│   └── raw_data.csv
│
├── results/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py


Packages to use:

beautifulsoup4
lxml
pandas
matplotlib
requests

Set up the scraper:
In the scraper/ecommerce_scraper.py file, implement a class to handle HTTP requests and extract product data from the e-commerce website using Beautiful Soup.

Create a parser:
In the scraper/parser.py file, implement a class to parse and extract structured data from the HTML content returned by the scraper.

Data cleaning:
In the analysis/data_cleaner.py file, implement a class to clean the extracted data and format it into a structured format (e.g., CSV) using pandas.

Data analysis and visualization:
In the analysis/visualizer.py file, implement a class to analyze and visualize the cleaned data using pandas and matplotlib. You can create various plots, such as bar charts, pie charts, and line graphs, to display relevant information about the products.

Main script:
In the main.py file, implement the main script that orchestrates the scraping process, data cleaning, and analysis. The script should save the raw data and the visualizations as output files in the respective folders.

Documentation:
Create a README.md file to document the project, its purpose, how to set it up, and how to run it. Provide clear instructions for users who may want to use or contribute to your project.

Version control:
Use Git for version control and include a .gitignore file to exclude files and folders that should not be tracked (e.g., virtual environment, output files, etc.).

Unit tests:
Write unit tests for the scraper, parser, data cleaner, and visualizer classes to ensure their functionality and validate the correctness of the code.



Example for the main.py ---

import csv
from scraper.ecommerce_scraper import EcommerceScraper
from scraper.parser import Parser

# Define the product URLs you want to scrape
product_urls = [
    'https://www.example.com/product/1',
    'https://www.example.com/product/2',
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

This main.py script does the following:

Imports the EcommerceScraper and Parser classes from the scraper package.
Defines the product URLs to scrape and the output CSV file path.
Writes the header row for the CSV file.
Iterates through the product URLs, scraping data using the EcommerceScraper and parsing it with the Parser.
Writes the parsed product data to the CSV file.

ALSO ADD for data cleaning, this code for main:

from analysis.data_cleaner import DataCleanser

input_file = 'data/raw_data.csv'
output_file = 'data/cleaned_data.csv'

data_cleanser = DataCleanser(input_file, output_file)
data_cleanser.clean_data()

ADDITION visualiser

from analysis.data_visualizer import DataVisualizer

input_file = 'data/cleaned_data.csv'

data_visualizer = DataVisualizer(input_file)
data_visualizer.visualize_data()

FOR MAIN

from analysis import DataCleanser, DataVisualiser