product_price=[10000,2020,34,56,775,89900,450]
def filter_Data(price):
    return price<1000
new_prices=list(filter(filter_Data,product_price))
print(product_price)
print(new_prices)