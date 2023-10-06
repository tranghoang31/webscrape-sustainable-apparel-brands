def jannjune():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    category = {
        'Blazers': 'https://jannjune.com/collections/blazer-coats-womenswear',
        'Blouses': 'https://jannjune.com/collections/blouses-womenswear',
        'Longsleeves': 'https://jannjune.com/collections/longsleeves',
        'Bottoms': 'https://jannjune.com/collections/bottoms-womenswear',
        'Shorts': 'https://jannjune.com/collections/shorts',
        'Dresses': 'https://jannjune.com/collections/dressesjumpsuits-womenswear',
        'Tops': 'https://jannjune.com/collections/tops-womenswear',
        'Skirts': 'https://jannjune.com/collections/skirts',
        'Sweats': 'https://jannjune.com/collections/sweaters-cardigans-womenswear'
    }

    # ---------------------------
    def get_price_data(source):
        prices = []
        check_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z"]

        driver.get(source)

        # ----------------------
        # Check number of page (45 products = 1 page)
        for element in driver.find_elements(By.XPATH,'//*[@id="CollectionAjaxContent"]/div/div/div[2]/div/div[3]/div[1]/div[2]'):
            count = element.text

        num_product = count.translate({ord(char): None for char in check_character})
        if int(num_product) % 45 > 0:
            page = (int(num_product) // 45) + 1
        else:
            page = int(num_product) // 45
        # ----------------------

        for i in range(1, page+1):
            i = str(i)
            driver.get(source + '?page=' + i)

            # Get all available product information
            product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'grid-product__meta')))

            # Get prices
            for product_element in product_elements:
                price_element = product_element.find_element(By.CLASS_NAME, 'grid-product__price')
                price = price_element.text
                prices.append(price)

            # Data Cleaning: Remove Wrong Data Format (non-numerical data)
            temp_price = prices.copy()
            for string in temp_price:
                if any(char in string for char in check_character):
                    prices.remove(string)
                if string[1] == '0':
                    prices.remove(string)

        return prices

    # ------------------------
    def get_avg_price(cat_name, src):

        for_avg = []
        prices = get_price_data(src)

        # Convert price into integer for further avg price aggregation
        price_list = []
        for i in prices:
            price_blazer = int(i[1:][:-3])
            for_avg.append(price_blazer)
            price_list.append(i)

        # ------------------------
        # Price Aggregation
        avg_price = sum(for_avg) / len(for_avg)

        print("---------  JANNJUNE - ", cat_name, "  ---------")
        print("Price List: ", price_list[:])
        print("No. of Products: ", len(price_list))
        print("Average Price: ", round(avg_price, 2))

    for cat, url in category.items():
        get_avg_price(cat, url)
