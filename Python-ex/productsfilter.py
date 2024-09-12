products=[
    {'id':1,'name':'Marker Pen', 'category':'st'},
	{'id':2,'name':'Sugar', 'category':'gr'},
	{'id':3,'name':'Pens', 'category':'st'},
	{'id':4,'name':'Millet', 'category':'gr'},
	{'id':5,'name':'Duster', 'category':'st'},
	{'id':6,'name':'Dal', 'category':'gr'}
    ]
def filterdata(product):
    if product['category']=='st':
        return True
    else:
        return False
    
# filter_obj=filter(filterdata,products)
# st_products=list(filter_obj)
# print(st_products)
print(list(filter(filterdata,products)))