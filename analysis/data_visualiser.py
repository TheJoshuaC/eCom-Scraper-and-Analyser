import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class DataVisualiser:

    """ 
    Initialize the class with the input file. The input file is the output file 
    from the DataCleanser class which is saved in the data folder.
    """
    def __init__(self, input_file, save_plots=False):
        self.input_file = input_file
        self.save_plots = save_plots

        if self.save_plots:
            self.create_plots_folder()

    def create_plots_folder(self):
        if not os.path.exists('plots'):
            os.makedirs('plots')

    """Read the data from the input file. The read data is stored in the df attribute as a pandas DataFrame."""
    def read_data(self):
        self.df = pd.read_csv(self.input_file)

    """Save the plot to the plots folder."""
    def save_plot(self, plot_name):
        if self.save_plots:
            plt.savefig(f'plots/{plot_name}.png', bbox_inches='tight')

    """Plot the price distribution using a histogram. The plot is saved in the plots folder."""
    def plot_price_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['price'], kde=True)
        plt.title('Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()
        self.save_plot('price_distribution')

    def plot_rating_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.countplot(x='rating', data=self.df)
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.show()
        self.save_plot('rating_distribution')

    def plot_top_brands(self, top_n=10):
        plt.figure(figsize=(14, 6))
        top_brands = self.df['brand'].value_counts().head(top_n).reset_index()
        top_brands.columns = ['brand', 'count']
        sns.barplot(x='brand', y='count', data=top_brands)
        plt.title(f'Top {top_n} Brands')
        plt.xlabel('Brand')
        plt.ylabel('Count')
        plt.show()
        self.save_plot('top_brands')

    def plot_top_categories(self, top_n=10):
        plt.figure(figsize=(14, 6))
        top_categories = self.df['category'].value_counts().head(top_n).reset_index()
        top_categories.columns = ['category', 'count']
        sns.barplot(x='category', y='count', data=top_categories)
        plt.title(f'Top {top_n} Categories')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.show()
        self.save_plot('top_categories')

    def plot_top_tags(self, top_n=10):
        plt.figure(figsize=(14, 6))
        top_tags = self.df['tags'].value_counts().head(top_n).reset_index()
        top_tags.columns = ['tags', 'count']
        sns.barplot(x='tags', y='count', data=top_tags)
        plt.title(f'Top {top_n} Tags')
        plt.xlabel('Tags')
        plt.ylabel('Count')
        plt.show()
        self.save_plot('top_tags')

    
    """Visualize the data by calling the above methods."""
    def visualize_data(self):
        self.read_data()
        self.plot_price_distribution()
        self.plot_rating_distribution()
        self.plot_top_brands()
        self.plot_top_categories()
        self.plot_top_tags()