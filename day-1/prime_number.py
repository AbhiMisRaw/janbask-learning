num = int(input("Please Eneter a number to check It's prime or not :"))

if num <= 3 and num >= 1:
    print(f"{num} is Prime Number")
else:
    i = 2
    while i < num - 1:
        if num % i == 0:
            print(f"{num} is divied by {i}, {num} is not Prime")
            break
        i += 1
    else:
        print(f"{num} is Prime Number")
