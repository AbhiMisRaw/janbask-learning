### String in Python is immutable means you can't change it after declareation.
### We can get a single character by its index

name = "Abhishek Mishra"

# you can use string slices to copy a part of string

# In Python 3 : all strings are unicode

print(f"Length of {name} is {len(name)}")
# [start(included) : end (excluded) : Steps ]
first_name = name[0:8]
last_name = name[9 : len(name)]

# printing Id of this string Object
print(f"{id(name)}")
print(f"{first_name}, {last_name}")
print(f"{id(first_name)}, {id(last_name)}")

# Some basic string function

print(f"{name} using upper -> {name.upper()}")
print(f"{name} using lower -> {name.lower()}")
print(f"{name} using capitalize -> {name.capitalize()}")

# searching operation is case sensitive
print(f"'m' in {name} at location : {name.find('m')}")
print(f"'M' in {name} at location : {name.find('M')}")

banana = "banana"
# replace
print(f"Replacing 'a' with 'x' in {banana} : {banana.replace('a','x')}")

fruits = "Apple Guava Blueberries Mango Orange Banana Cucumber Papaya"
fruits_list = fruits.split(" ")
print(f"Converting this String {fruits} to List: {fruits_list}")

email = "abhi.janbask@gmail.com"
username = email.split("@")[0]
domain = email.split("@")[1]
print(f"Username : {username} ")
print(f"Domain {domain}")
