import json

fp1=open('products.json','r')
products=json.load(fp1)
print('open successfully')
fp2=open('beauty.json','w')
json.dump(products,fp2)
print('writed successfully')

fp1.close()
fp2.close()

