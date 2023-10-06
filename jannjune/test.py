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

driver.get("https://jannjune.com/collections/tops-womenswear?page=3")

product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'grid-product__meta')))

# Get prices
for product_element in product_elements:
    price_element = product_element.find_element(By.CLASS_NAME, 'grid-product__price')
    price = price_element.text
    prices.append(price)

# Data Cleaning: Remove Wrong Data Format (non-numerical data)
temp = []
for i in prices:
    temp.append(i)
for string in temp:
    if any(char in string for char in check_character):
        prices.remove(string)
    if string[1] == '0':
        prices.remove(string)

print(prices)
