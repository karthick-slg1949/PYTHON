import pymongo
client= pymongo.MongoClient('mongodb://localhost:27017/')
db=client['pythondata']
user_col=db['json']
query={"id":2}
user_col.delete_one(query)

print("Deleted successfully!")
client.close()