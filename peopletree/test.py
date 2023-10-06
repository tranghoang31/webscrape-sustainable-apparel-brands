from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

prices = []
check_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v", "w", "x", "y", "z"]

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

source = "https://byherth.com/collections/tops"
driver.get(source)

# Get all available product information
product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ProductItem__Info ProductItem__Info--center')))

print(product_elements)
# Get prices
for product_element in product_elements:
    price_element = product_element.find_element(By.CLASS_NAME, 'ProductItem__Price Price Text--subdued')
    price = price_element.text
    print(price)
    prices.append(price)

print(prices)

# Data Cleaning: Remove Wrong Data Format (non-numerical data)
# temp_price = prices.copy()
# for string in temp_price:
#     if any(char in string for char in check_character):
#         prices.remove(string)
#     if string[1] == '0':
#         prices.remove(string)
#
# print(prices)