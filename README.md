# Data-Scraping-and-Analysis
## Jumia Tech Week Products Dashboard
This project provides an interactive dashboard to analyze and visualize Jumia Tech Week products using Streamlit. The dashboard allows filtering and visualizing product data, including prices, discounts, and more.

## Table of Contents
Installation
Usage
Features
Data Cleaning
Visualizations
Installation
Clone the Repository:

### Clone the repository to your local machine using the provided GitHub URL.
Install the Required Packages:

### Use pip to install the necessary packages: pandas, streamlit, matplotlib, and seaborn.
Run the Streamlit App:

### Execute the Streamlit app to start the dashboard.

# Usage

Loading Data: The application loads data from a CSV file containing Jumia Tech Week products.
Data Cleaning: Prices and discounts are cleaned and converted to numeric values for analysis.
Filtering: Use the sidebar to filter products based on discount percentage and price range.
Visualizations: Various charts and plots are available to visualize the data.
Features
Filter Options: Adjust the discount percentage and price range to filter products.
Data Table: View the filtered product data in a tabular format.
Basic Statistics: Display basic statistical information about the filtered data.
Interactive Charts: Explore visualizations like bar charts, line charts, scatter plots, and pie charts.


## Data Cleaning
The data cleaning process includes:

Removing Non-Numeric Characters: Stripping currency symbols and commas from price and old price fields.
Converting to Numeric Values: Converting cleaned price and old price fields to numeric data types.
Extracting Discount Percentage: Removing percentage symbols from discount fields and converting them to numeric values.
Visualizations
Average Price per Discount Range: A bar chart showing the average price for each discount range.
Price Trend: A line chart displaying the trend of product prices.
Old Price vs New Price Scatter Plot: A scatter plot comparing old prices to new prices.
Discount Distribution Pie Chart: A pie chart illustrating the distribution of discounts across products.