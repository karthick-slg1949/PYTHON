import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['11am']
user_col=db['user']
user_col.update_one({'id':1,'first_name':'Krish','gender':'Male'})

client.close()