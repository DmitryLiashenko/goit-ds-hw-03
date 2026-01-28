from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
from func_for_db import (
    show_all,
    show_name,
    updtate_age,
    add_features,
    dell_name,
    dell_all,
    parse_input
)

client = MongoClient("mongodb://localhost:27017/")
db = client.test_db
collection = db.users


# delete all in collection befor start
collection.delete_many({})

# update db after start
cats = [
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    },
    {
        "name": "murzik",
        "age": 5,
        "features": ["любить коробки", "спить на ноутбуці", "сірий"],
    },
    {
        "name": "pushok",
        "age": 2,
        "features": ["дуже пухнастий", "боїться пилососа", "білий"],
    },
    {
        "name": "chernysh",
        "age": 4,
        "features": ["нічний мисливець", "дивиться в стіну", "чорний"],
    },
    {
        "name": "sirko",
        "age": 1,
        "features": ["дуже активний", "краде їжу", "смугастий"],
    },
]
collection.insert_many(cats)


def main():
    """Main function"""
    print("Welcome to the db_cats")
    while True:
        print("I Can Help You with Yuor Cats")
        print("Command:",
        "Show_all -- показать все записи",
        "Show_name -- показать всю инфолрмацию по имени",
        "update_age -- изменить возраст по имени",
        "add_features -- добавить способность\\описание",
        "dell_name -- удалить по имени",
        "dell_all -- удалить всю информацию о котах",
        "exit\\close -- выход",
        sep="\n")
        print()

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "show_all":
            pass
        elif command == "show_name":
            pass
        elif command == "updtate_age":
            pass
        elif command == "add_features":
            pass
        elif command == "dell_name":
            pass
        elif command == "dell_all":
            dell_all(collection)
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
