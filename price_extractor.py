# Step 1 - Install Reauired libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from datetime import datetime

# --- Website Link Set Up-----
base_url = "https://www.citymall.com.mm/citymall/my/c/id05011"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# --- Robust Extraction Functions ---
def extract_product_name(tag):
    product_name_tag = tag.find('a', class_='name')
    return product_name_tag.get_text(strip=True) if product_name_tag else "N/A"

def extract_product_price(tag):
    product_price_tag = (tag.find("span", class_="product-sale-price") or tag.find("p", class_="product-price"))
    if product_price_tag:
        price_text = product_price_tag.get_text(strip=True)
        price_digits = re.findall(r"\d+", price_text)
        return int("".join(price_digits)) if price_digits else 0
    return 0

def extract_product_status(tag):
    product_status_tag = tag.find('p', class_='product-seller')
    return product_status_tag.get_text(strip=True) if product_status_tag else "N/A"

# Create empty lists to store extracted data
product_name_list = [] # to store extracted product name
product_price_list = [] # to store extracted product price
product_status_list = []  # to store extracted product status

# Loop through all 18 pages
for i in range(0, 18): 
    current_url = f"{base_url}?page={i}"
    print(f"Scraping: {current_url}")
    
    try:
        # request the page INSIDE the loop
        response = requests.get(current_url, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"Failed to load page {i}")
            continue
            
        soup = BeautifulSoup(response.text, "html5lib")
        main_tags = soup.find_all('div', class_='product-info')

        for dummy_tag in main_tags:
            # Use the safe functions defined above
            product_name_list.append(extract_product_name(dummy_tag))
            product_price_list.append(extract_product_price(dummy_tag))
            product_status_list.append(extract_product_status(dummy_tag))

        time.sleep(1) # Delay to prevent getting blocked
    except Exception as e:
        print(f"Error on page {i}: {e}")

# Export data as an Excel file.
data_dic = {
    "Product Name": product_name_list,
    "Product Price": product_price_list,
    "Product Status": product_status_list
}

# Create a dataframe
df = pd.DataFrame(data_dic)
time_str = datetime.now().strftime("%H-%M-%S")
filename = f"Output_{time_str}.xlsx"
df.to_excel(filename, index=False)
print(f"All steps completed! Saved to {filename}")