product_price=[1000,10000,29,340,45,567,789]
new_product_price=[]
#display all product price below 1000
for price in product_price:
    if price<1000:
        new_product_price.append(price)

print(new_product_price) 
print(product_price)