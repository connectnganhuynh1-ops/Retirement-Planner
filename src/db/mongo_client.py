import os
from pymongo import MongoClient

def get_db():
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(uri)
    return client["retirement_planner"]
