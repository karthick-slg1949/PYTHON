import requests
import json
import csv

api_url='https://jsonplaceholder.typicode.com/users1'
users_data=None
user=None

try:
    users_data=requests.get(api_url)
    # print(users.status_code)
    user=users_data.json()
    users_data.raise_for_status()
    
except requests.exceptions.RequestException as e:
    fp=open('user.json','r')
    user=json.load(fp)

print(type(user))
print(user)

