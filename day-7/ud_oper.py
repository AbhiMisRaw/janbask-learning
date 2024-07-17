import sqlite3

try:
    conn = sqlite3.connect("data.sqlite")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM User""")
    result = cursor.fetchall()

    for tup in result:
        print(tup)

    while True:
        print("For Updation press 1, delete press 2")
        num = int(input())
        if num == 1:
            print("Which Data you want to update\nEnter the Id")
            id = int(input())
            print("What you want to update:\n For Name press 1,for age press 2")
            x = int(input())
            if x == 1:
                print("Enter the Name :")
                name = input()
                cursor.execute("""UPDATE User SET name=? WHERE id=?""", (name, id))
            else:
                print("Please Enter Your age :")
                age = int(input())
                cursor.execute("""UPDATE User SET age=? WHERE id=?""", (age, id))
            conn.commit()
        elif num == 2:
            print("Which Data you want to update\nEnter the Id")
            id = int(input())
            cursor.execute("DELETE FROM User WHERE id = ?", (id,))
            conn.commit()
        else:
            break

except:
    pass
finally:
    conn.close()
