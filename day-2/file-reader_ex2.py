file_name = input("Enter a file name >>> ")

try:
    file = open(file_name)
except FileNotFoundError:
    print("Sorry, this file doesn't exist!")
    quit()

print("Content of files are :")
for line in file:
    print(line.strip())
