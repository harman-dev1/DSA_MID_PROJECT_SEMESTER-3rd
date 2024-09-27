from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# Lists for storing Data
type_of_product = []
name_of_product = []
price_of_product = []
sold_products = []
discount_on_products = []
delivery_charges = []
rating_of_products = []
out_of_stock = []
brand_Name = []

# Scraping Data From Website
base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=painting&_sacat=0&LH_TitleDesc=0&_pgn="
for page in range(1, 167):
    print("Page No:", page)
    url = base_url + str(page)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    blocks = soup.find_all("div", class_='s-item__info clearfix')
    if not blocks:
        print("None")
        break
    for b in blocks:
        name = b.find("div", class_='s-item__title').text
        price = b.find("span", class_='s-item__price').text
        sold = b.find("span", class_='s-item__dynamic s-item__quantitySold')
        discount = b.find("span", class_='s-item__discount s-item__discount')
        charges = b.find("span", class_='s-item__shipping s-item__logisticsCost')
        ratings = b.find("div", class_='x-star-rating')
        brand = str(name).split(" ")
        stock = b.find("span", class_='s-item__dynamic s-item__almostGone')
        if sold:
            s_prdct = sold.text
        else:
            s_prdct = "NA"
        if discount:
            dis = discount.text
        else:
            dis = "NA"
        if charges:
            ch = charges.text
        else:
            ch = "NA"
        if len(brand) == 1:
            n_brand = brand[0]
        else:
            n_brand = brand[1]
        if ratings:
            rat = ratings.text
        else:
            rat = "NA"
        if stock:
            stck = stock.text
        else:
            stck = "Available"
        TYPE = "Painting"
        type_of_product.append(TYPE)
        name_of_product.append(name)
        price_of_product.append(price)
        sold_products.append(s_prdct)
        discount_on_products.append(dis)
        delivery_charges.append(ch)
        rating_of_products.append(rat)
        out_of_stock.append(stck)
        brand_Name.append(n_brand)
    time.sleep(2)

# Create a DataFrame from the lists
data_df = pd.DataFrame({
    'Type Of Product': type_of_product,
    'Name Of Product': name_of_product,
    'Brand Name': brand_Name,
    'Out Of Stock': out_of_stock,
    'Price Of Products': price_of_product,
    'Discount On Product': discount_on_products,
    'Delivery Charges': delivery_charges,
    'Sold Products': sold_products,
    'Ratings': rating_of_products
})

# Saving Data Frame To Excel
data_df.to_excel('Painting.xlsx', index=False)
print("Data saved in Excel File successfully!!!")
