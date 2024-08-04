from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")

db = client.my_database
collection = db.my_collection

document = collection.find_one({"_id": "counter"})
if document is None:
    collection.insert_one({"_id": "counter", "number": 1})
    next_number = 1
else:
    result = collection.update_one({"_id": "counter"}, {"$inc": {"number": 1}})
    next_number = document["number"] + 1

print("Python container exited")

client.close()
