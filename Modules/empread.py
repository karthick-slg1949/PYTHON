import csv

fp=open('emp.csv','r')
rows=csv.reader(fp)
users=list(rows)
print(type(rows))
for user in users[2:]:
    print(user[2])