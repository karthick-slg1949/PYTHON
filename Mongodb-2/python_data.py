import requests
user_data=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=user_data.json()
new_user_list=[]
for user in user_list:
    new_user_list.append({'id':user['id'],
                         'user_name':user['name'],
                         'city':user['address']['city']
                         })
    
print(user_list)