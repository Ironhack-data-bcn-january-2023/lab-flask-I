from pymongo import MongoClient

client = MongoClient("localhost:27017")
db = client["Ironhack"]
client.list_database_names()
c = db.get_collection("Employees")