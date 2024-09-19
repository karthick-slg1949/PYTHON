import csv

customers=[{'eid':101,'name':'karthi','avail':True},
           {'eid':102,'name':'satheesh','avail':False},
           {'eid':103,'name':'dinesh','avail':True},
           {'eid':104,'name':'rahul','avail':False}
           ]
fp2=open('employee.csv','w',newline='')
wr=csv.writer(fp2)
wr.writerow(['eid','name','avail'])
for cust in customers:
    wr.writerow([cust['eid'],cust['name'],cust['avail']])
print('csv file created successfully')

fp2.close()

