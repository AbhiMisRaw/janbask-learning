import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect("data.sqlite")

# cursor object
cursor_obj = connection_obj.cursor()

statement = """SELECT * FROM User"""

cursor_obj.execute(statement)

print("All the data")

output = cursor_obj.fetchall()

for row in output:
    cursor_obj.execute("""UPDATE User SET age=(?) where name=(?)""", (20, "Lexy"))
    print(f"{row[0]} | {row[1]} | {row[2]}")

connection_obj.commit()
# Close the connection
connection_obj.close()
