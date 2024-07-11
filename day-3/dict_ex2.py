### Counting words in a file

file = open("loreum.txt")

counter = {}

for line in file:
    words = line.split()
    for word in words:
        counter[word] = counter.get(word, 0) + 1

file.close()

file2 = open("word-counter.txt", "w")


file2.write(str(counter))

file2.close()
