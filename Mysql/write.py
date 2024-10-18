import pymongo
import json
import requests

users=None
users_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_data.json()

fp=open('user.json','w')
json.dump(users,fp)
print("Data written successfully")
fp.close()