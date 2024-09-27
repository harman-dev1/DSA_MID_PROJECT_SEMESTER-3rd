import pandas as pd
#import funcs
    
# Read the Excel file into a DataFrame
excel_file = "All_scrap_data.xlsx"
data_df = pd.read_excel(excel_file,nrows=400)

# Access data from the DataFrame
type_of_product = data_df['Type Of Product'].tolist()
name_of_product = data_df['Name Of Product'].tolist()
brand_Name = data_df['Brand Name'].tolist()
out_of_stock = data_df['Out Of Stock'].tolist()
price_of_product = data_df['Price Of Products'].tolist()
discount_on_products = data_df['Discount On Product'].tolist()
delivery_charges = data_df['Delivery Charges'].tolist()
sold_products = data_df['Sold Products'].tolist()
rating_of_products = data_df['Ratings'].tolist()


eBay = []
def make_2d_ebay_data():
    for i in range(0,400):
        temp = {'Type Of Product':'empty',
                'Name Of Product':'empty',
                'Brand Name':'empty',
                'Out Of Stock':'empty',
                'Price Of products':0,
                'Discount On Product':0,
                'Delivery Charges':0,
                'Sold Products':0,
                'Ratings':0}
        temp['Type Of Product'] = type_of_product[i]
        temp['Name Of Product'] = name_of_product[i]
        temp['Brand Name'] = brand_Name[i]
        temp['Out Of Stock'] = out_of_stock[i]
        #splitting of prices
        if (price_of_product[i] == 0.0 or price_of_product[i] == ""):
            split_price = float(0)
        else:
            try:
                split_price = str(price_of_product[i]).split(" ")
                split_price = split_price[0]
                if(split_price[0] == "$"):
                    split_price = float(split_price[1]+split_price[2]+split_price[3]) 
            except:
                split_price = float(0)
        temp['Price Of products'] = split_price
        #splitting of Discounts
        if(discount_on_products[i] == 0.0 or discount_on_products[i] == "" or discount_on_products[i] == " " or discount_on_products[i] == "nan"):
            split_discount = int(0)
        else:
            try:
                split_discount = str(discount_on_products[i]).split("%")
                split_discount = int(split_discount[0])
            except ValueError:
                split_discount =float(0)
        temp['Discount On Product'] = split_discount
        #splitting of Delivery
        if(delivery_charges[i] == 0.0 or delivery_charges[i] == ""):
            split_delivery = float(0)
        else:
            split_delivery = str(delivery_charges[i]).split(" ")  
            split_delivery = split_delivery[0]
            if(split_delivery == ""):
                split_delivery = float(0)
            else:
                if split_delivery and "$" in split_delivery:
                    split_delivery = split_delivery.split("$")[1]
                    try:        
                        split_delivery = float(split_delivery)
                    except ValueError:
                        split_delivery = float(0) 
                else:
                    split_delivery = float(0) 
        temp['Delivery Charges'] = split_delivery
        #splitting products
        if(sold_products[i] == 0.0 or sold_products[i] == "" or sold_products[i] == "nan" or sold_products[i] == "na"):
            split_sold = int(0)
        else:
            try:
                split_sold = str(sold_products[i]).split(" ")
                split_sold = int(split_sold[0])
            except ValueError:
                split_sold = int(0)           
        temp['Sold Products'] = split_sold
        #splitting Ratings
        if(rating_of_products[i] == 0.0 or rating_of_products[i] == ""):
            split_rating = float(0)
        else:
            try:
                split_rating = str(rating_of_products[i]).split(" ")
                split_rating = float(split_rating[0])
            except:
                split_rating = float(0)
        temp['Ratings'] = split_rating
        eBay.append(temp)
    return eBay

eBay = make_2d_ebay_data()
