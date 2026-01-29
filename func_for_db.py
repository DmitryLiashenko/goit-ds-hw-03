from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi

#decorator for func try except
def input_error(func):
    """Decorator for handling input errors."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Something wrong {e}"

    return inner


@input_error
def show_all(collection):
    return list(collection.find())


@input_error
def show_name(collection,name):
    return collection.find_one({"name": name})


@input_error
def update_age(collection,name,age):
    collection.update_one({"name": name}, {"$set": {"age": age}})
    result = collection.find_one({"name": name})
    return result


@input_error
def add_features(collection,name,features):
    collection.update_one({"name": name}, {"$push": {"features": features}})
    result = collection.find_one({"name": name})
    return result


@input_error
def dell_name(collection,name):
    collection.delete_one({"name": name})
    result = collection.find_one({"name": name})
    return result

@input_error
def dell_all(collection):
    collection.delete_many({})
    
    print("DB Clear")
