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