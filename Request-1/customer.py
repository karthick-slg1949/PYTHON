import json
# import csv
customers=[{'eid':101,'name':'karthi','avail':True},
           {'eid':102,'name':'satheesh','avail':False},
           {'eid':103,'name':'dinesh','avail':True},
           {'eid':104,'name':'rahul','avail':False}
           ]
fp1=open('emp.json','w')
# fp2=open('emp.csv','w')
json.dump(customers,fp1)
print('json file created successfully')

fp1.close()

