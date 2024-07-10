reader = open("hello.txt")
print(f"{reader} and it's type : {type(reader)}")

reader2 = open("loreum.txt", "r")
print(f"{reader2} and it's type : {type(reader2)}")

text = reader2.read()
print(f"Length of the file is : {len(text)}")
print(text)

char = input("Enter a starting character in line you want to search : ")

for line in reader2:
    line = line.strip()
    if line.startswith(char):
        print(line)


reader.close()
reader2.close()
