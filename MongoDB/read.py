import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['11am']
user_collection=db['user']
user_list=user_collection.find()

print(type(user_collection))
print(type(user_list))

for user in user_list:
    print(user['first_name'])

client.close()
    