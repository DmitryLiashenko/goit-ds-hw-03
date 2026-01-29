from pymongo.mongo_client import MongoClient
from func_for_db import (
    show_all,
    show_name,
    update_age,
    add_features,
    dell_name,
    dell_all,
)


client = MongoClient("mongodb://localhost:27017/")
db = client.test_db
collection = db.cat


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
        print()
        print("I Can Help You with Your Cats")
        print()
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

        command = input("Enter a command: ")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "show_all":
            print(show_all(collection))
        elif command == "show_name":
            name = input("enter cat name:").lower()
            print(show_name(collection,name))
        elif command == "update_age":
            print("input name and age")
            name, age = input().split()
            print(update_age(collection,name.lower(),age))
        elif command == "add_features":
            name, feautures = input("wright name and features:").split()
            print(add_features(collection,name.lower(),feautures))
        elif command == "dell_name":
            name = input("write name:")
            print(dell_name(collection,name.lower()))
        elif command == "dell_all":
            dell_all(collection)
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
