prices=[199,99,75,65,1999,2001,4000,6000]

def get_products_price(price):
    return price>2000
print(list(filter(get_products_price,prices)))