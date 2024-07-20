from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome for scraping without GUI
chrome_options.add_argument("--disable-gpu")

# Set up the Chrome driver
driver_service = Service('chromedriver.exe')  # Update with your path to chromedriver
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Open Jumia Tech Week page
driver.get('https://www.jumia.co.ke/mlp-tech-week/')

# Wait for products to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.prd._fb.col.c-prd')))

# Extract page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.quit()

# Extract product details
products = soup.find_all('article', class_='prd _fb col c-prd')
data = []

for product in products:
    try:
        title = product.find('h3', class_='name').text.strip()
    except:
        title = None

    try:
        price = product.find('div', class_='prc').text.strip()
    except:
        price = None

    try:
        old_price = product.find('div', class_='old').text.strip() if product.find('div', class_='old') else None
    except:
        old_price = None

    try:
        discount = product.find('div', class_='bdg _dsct _sm').text.strip() if product.find('div', class_='bdg _dsct _sm') else None
    except:
        discount = None

    try:
        rating = product.find('div', class_='stars _s').text.strip() if product.find('div', class_='stars _s') else None
    except:
        rating = None

    product_data = {
        'title': title,
        'price': price,
        'old_price': old_price,
        'discount': discount,
        'rating': rating
    }
    data.append(product_data)

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('jumia_techweek_products.csv', index=False)

print(df)