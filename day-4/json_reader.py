import json

file = open("data.json")

# json.load() takes an string and parse it and convert it to a json object.
data = json.load(file)

print(data)
print(type(data))

file.close()

# user = {}
# for entry in data:
#     user[entry["name"]] = entry["age"]

user = {entry["name"]: entry["age"] for entry in data}

print(type(user))
print(user)

user_sorted_by_age = sorted([(age, name) for (name, age) in user.items()])
print(user_sorted_by_age)
totle_user = len(user_sorted_by_age)
print("****** USER *******")
print(f"Total User : {totle_user}")
print(
    "10 ages person in this Group : ",
    user_sorted_by_age[-1:],
)
