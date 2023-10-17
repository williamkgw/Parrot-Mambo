from pymongo.mongo_client import MongoClient

def start_client_database_connection(uri):
    return MongoClient(uri)

def database(client, name):
    return client[name]

def collection(database, name):
    return database[name]

def find_in_collection(collection, search = None, projection = None):
    return collection.find_one(search, projection)

def find_many_in_collection(collection, search = None, projection = None):
    return collection.find(search, projection)

def insert_in_collection(collection, data):
    return collection.insert_one(data)

def insert_many_in_collection(collection, data):
    return collection.insert_many(data)
