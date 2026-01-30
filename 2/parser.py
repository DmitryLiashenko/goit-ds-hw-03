from connect_to_db import get_client


client = get_client()
if client:
    db = client.my_database
    collection = db.my_collection


    
