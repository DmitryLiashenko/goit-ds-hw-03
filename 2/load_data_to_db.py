from connect_to_db import get_client
import json


def load_data():
    client = get_client()
    if not client:
        return
    db = client.quotes_db  
    quotes_collection = db.quotes
    authors_collection = db.authors

    try:
        with open("quotes.json", "r", encoding="utf-8") as f:
            quotes = json.load(f)
        quotes_collection.insert_many(quotes)

        with open("authors.json", "r", encoding="utf-8") as f:
            authors = json.load(f)
        authors_collection.insert_many(authors)
    except Exception as e:
        print(f"Something wrong {e}")
        


if __name__ == "__main__":
    load_data()
