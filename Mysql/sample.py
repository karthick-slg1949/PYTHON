import requests
import json
import mysql.connector

users_data = requests.get('https://jsonplaceholder.typicode.com/users')
users = users_data.json()

with open('user.json', 'w') as fp1:
    json.dump(users, fp1)
print("User Data - written into JSON file successfully")

new_user = []
for user in users:
    new_user.append((user['id'], user['name'], user['email'], user['address']['city'], user['website'], user['phone']))

print(new_user)

con = mysql.connector.connect(host='localhost', user='root', password='root', database='hello')
cursor = con.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS user (
    uid INT PRIMARY KEY,
    uname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    city VARCHAR(255),
    website VARCHAR(255),
    phone VARCHAR(255)
);
"""
cursor.execute(create_table_query)

sql_st = 'INSERT INTO user (uid, uname, email, city, website, phone) VALUES (%s, %s, %s, %s, %s, %s)'
cursor.executemany(sql_st, new_user)
con.commit()

print("Data inserted successfully into MySQL table")

cursor.close()
con.close()
