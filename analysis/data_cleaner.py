import pandas as pd

class DataCleanser:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    """Read the data from the input file."""
    def read_data(self):
        self.df = pd.read_csv(self.input_file)

    """Write the data to the output file."""
    def write_data(self):
        self.df.to_csv(self.output_file, index=False)

    """Remove missing values from the data."""
    def remove_missing_values(self):
        self.df.dropna(inplace=True)

    """Clean the price column by removing commas and dollar signs, and converting the data type to float."""
    def clean_price(self):
        self.df['price'] = self.df['price'].str.replace(',', '').str.replace('$', '').astype(float)

    """Clean the rating column by removing the 'out of 5 stars' text, and converting the data type to float."""
    def clean_description(self):
        self.df['description'] = self.df['description'].str.replace('Description', '').str.strip()

    """Clean the rating column by removing the 'out of 5 stars' text, and converting the data type to float."""
    def clean_rating(self):
        self.df['rating'] = self.df['rating'].str.replace(' out of 5 stars', '').astype(float)

    """Clean the reviews column by removing the 'reviews' text, and converting the data type to int."""
    def clean_reviews(self):
        self.df['reviews'] = self.df['reviews'].str.replace(' reviews', '').astype(int)

    """Clean the availability column by converting the values to 1 and 0."""
    def clean_availability(self):
        self.df['availability'] = self.df['availability'].apply(lambda x: 1 if x == 'In Stock' else 0)

    """Clean the sku, brand, category, subcategory, tags, and url columns by removing the text before the colon."""
    def clean_sku(self):
        self.df['sku'] = self.df['sku'].str.replace('SKU: ', '')

    def clean_brand(self):
        self.df['brand'] = self.df['brand'].str.replace('Brand: ', '')

    def clean_category(self):
        self.df['category'] = self.df['category'].str.replace('Category: ', '')

    def clean_subcategory(self):
        self.df['subcategory'] = self.df['subcategory'].str.replace('Subcategory: ', '')

    def clean_tags(self):
        self.df['tags'] = self.df['tags'].str.replace('Tags: ', '')

    def clean_url(self):
        self.df['url'] = self.df['url'].str.replace('URL: ', '')

    """Clean the data by calling all the cleaning methods."""
    def clean_data(self):
        self.read_data()
        self.remove_missing_values()
        self.clean_price()
        self.clean_description()
        self.clean_rating()
        self.clean_reviews()
        self.clean_availability()  
        self.clean_sku()
        self.clean_brand()
        self.clean_category()
        self.clean_subcategory()
        self.clean_tags()
        self.clean_url()
        self.write_data()
    
    """Print the data."""
    def print_data(self):
        print(self.df)
# Path: analysis/data_cleaner.py