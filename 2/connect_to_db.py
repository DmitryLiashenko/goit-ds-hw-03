import os
from pymongo import MongoClient,errors
from dotenv import load_dotenv


load_dotenv() 
password = os.getenv("DB_PASSWORD")
client = MongoClient(f"mongodb+srv://dmliash1_db_user:{password}@cluster0.qhtl8tt.mongodb.net/?appName=Cluster0")


def get_client():
    try:
        client = MongoClient(
            f"mongodb+srv://dmliash1_db_user:{password}@cluster0.qhtl8tt.mongodb.net/?appName=Cluster0"
        )
        return client
    except errors.ServerSelectionTimeoutError as e:
        print("Не удалось подключиться к MongoDB:", e)
        return None
    except errors.OperationFailure as e:
        print("Ошибка аутентификации:", e)
        return None


# client = get_client()
# if client:
#     db = client.my_database
#     collection = db.my_collection
# next_page = "https://quotes.toscrape.com/page/2/"
