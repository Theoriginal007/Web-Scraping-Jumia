import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('jumia_techweek_products.csv')

# Convert price and old_price to numeric (remove non-numeric characters and convert to float)
df['price'] = df['price'].str.replace('KSh', '').str.replace(',', '')
df['old_price'] = df['old_price'].str.replace('KSh', '').str.replace(',', '')

# Convert to numeric with errors='coerce'
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['old_price'] = pd.to_numeric(df['old_price'], errors='coerce')

# Extract numeric discount percentage
df['discount'] = df['discount'].str.replace('%', '')
df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

# Streamlit app
st.title('Jumia Tech Week Products Dashboard')

# Streamlit sidebar for filters
st.sidebar.header('Filter Options')

# Filter by discount percentage
min_discount = st.sidebar.slider('Min Discount (%)', 0.0, 100.0, 0.0)
max_discount = st.sidebar.slider('Max Discount (%)', 0.0, 100.0, 100.0)

# Filter by price range
min_price = st.sidebar.slider('Min Price (KSh)', float(df['price'].min()), float(df['price'].max()), float(df['price'].min()))
max_price = st.sidebar.slider('Max Price (KSh)', float(df['price'].min()), float(df['price'].max()), float(df['price'].max()))

# Apply filters
filtered_df = df[(df['discount'] >= min_discount) & (df['discount'] <= max_discount) &
                 (df['price'] >= min_price) & (df['price'] <= max_price)]

# Display filtered data
st.write(f"### Showing {filtered_df.shape[0]} products")
st.dataframe(filtered_df)

# Display basic statistics
st.write("### Basic Statistics")
st.write(filtered_df.describe())

# Charts
st.header('Visualizations')

# Bar chart for average price per discount range
st.subheader('Average Price per Discount Range')
avg_price_per_discount = filtered_df.groupby('discount')['price'].mean().reset_index()
st.bar_chart(avg_price_per_discount.set_index('discount'))

# Line chart for price trend
st.subheader('Price Trend')
st.line_chart(filtered_df[['price']].reset_index(drop=True))

# Scatter plot of old price vs new price
st.subheader('Old Price vs New Price')
fig, ax = plt.subplots()
ax.scatter(filtered_df['old_price'], filtered_df['price'], alpha=0.5)
ax.set_xlabel('Old Price (KSh)')
ax.set_ylabel('New Price (KSh)')
ax.set_title('Old Price vs New Price')
st.pyplot(fig)

# Pie chart of discount distribution
st.subheader('Discount Distribution')
discount_counts = filtered_df['discount'].value_counts()
fig, ax = plt.subplots()
ax.pie(discount_counts, labels=discount_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Discount Distribution')
st.pyplot(fig)
