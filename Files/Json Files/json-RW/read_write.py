import json
fp1=open('users.json','r')
users=json.load(fp1)
print('data created successfully')
employee=[]
for user in users:
    employee.append({'eid':user['id'],
                     'ename':user['first_name'],
                     'email':user['email']
                     })
    fp2=open('emp.json','w')
    json.dump(employee,fp2)

    fp1.close()
    fp2.close()