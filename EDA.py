import pandas as pd

# Load the data
df = pd.read_csv('jumia_techweek_products.csv')

# Display the first few rows to understand the structure
print(df.head())

# Convert price and old_price to numeric (remove non-numeric characters and convert to float)
df['price'] = df['price'].str.replace('KSh', '').str.replace(',', '').astype(float)
df['old_price'] = df['old_price'].str.replace('KSh', '').str.replace(',', '').astype(float)

# Extract numeric discount percentage
df['discount'] = df['discount'].str.replace('%', '').astype(float)

# Display the cleaned data
print(df.head())
# Basic statistics
print("Basic Statistics:")
print(df.describe())

# Highest price
highest_price = df['price'].max()
print(f"Highest Price: KSh {highest_price}")

# Lowest price
lowest_price = df['price'].min()
print(f"Lowest Price: KSh {lowest_price}")

# Mean discount
mean_discount = df['discount'].mean()
print(f"Mean Discount: {mean_discount}%")

# Plotting (if necessary)
import matplotlib.pyplot as plt

# Plot histogram of prices
plt.figure(figsize=(10, 6))
df['price'].plot(kind='hist', bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Prices')
plt.xlabel('Price (KSh)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot boxplot of prices
plt.figure(figsize=(10, 6))
df['price'].plot(kind='box')
plt.title('Boxplot of Prices')
plt.ylabel('Price (KSh)')
plt.grid(True)
plt.show()

# Plot scatter plot of old price vs new price
plt.figure(figsize=(10, 6))
plt.scatter(df['old_price'], df['price'], color='skyblue', edgecolor='black')
plt.title('Old Price vs New Price')
plt.xlabel('Old Price (KSh)')
plt.ylabel('New Price (KSh)')
plt.grid(True)
plt.show()