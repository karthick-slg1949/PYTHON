import requests
import mysql.connector
import json
import csv
import pymongo

users=None
users_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_data.json()
print(users)
print(type(users))

