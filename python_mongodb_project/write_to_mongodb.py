from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")

db = client.my_database
collection = db.my_collection

document = {"message": "Hello, Sergey when do you come Ashotsk"}
insert_result = collection.insert_one(document)
print("Pyhon container exited")
client.close()
