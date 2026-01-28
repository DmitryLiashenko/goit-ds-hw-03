from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi


def input_error(func):
    """Decorator for handling input errors."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Something wrong {e}"

    return inner


@input_error
def parse_input(user_input):
    """Parse user input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def show_all(collection):
    pass


@input_error
def show_name(collection,name):
    pass


@input_error
def updtate_age(collection,name,age):
    pass


@input_error
def add_features(collection,name,features):
    pass


@input_error
def dell_name(collection,name):
    pass


@input_error
def dell_all(collection):
    collection.delete_many({})
