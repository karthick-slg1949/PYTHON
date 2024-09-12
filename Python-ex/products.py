products=[
    {'id':1,'name':'Marker Pen', 'category':'st'},
	{'id':2,'name':'Sugar', 'category':'gr'},
	{'id':3,'name':'Pens', 'category':'st'},
	{'id':4,'name':'Millet', 'category':'gr'},
	{'id':5,'name':'Duster', 'category':'st'},
	{'id':6,'name':'Dal', 'category':'gr'}
    ]
st_products=[]
gr_products=[]

for product in products:
    if product['category']=='st':
        st_products.append(product)
    else:
        gr_products.append(product)
print(st_products)
print(gr_products)