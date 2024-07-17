import json
import sqlite3

file_handler = open("data.json")

text = json.load(file_handler)

print(f"TYPE : {type(text)}")

# for x in text:
#     print(f"{x} {type(x)} : y")

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

cursor.executescript(
    """
DROP TABLE IF EXISTS User;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL);
"""
)

for entry in text:
    name = entry["name"]
    age = entry["age"]

    cursor.execute("""INSERT INTO User (name,age) VALUES (?, ?)""", (name, age))
    connection.commit()


connection.close()
