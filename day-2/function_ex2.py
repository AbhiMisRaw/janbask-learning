def is_prime(num):
    if num <= 3 and num >= 1:
        return True
    count = 2
    while count < num - 1:
        if num % count == 0:
            return False
        count += 1

    return True


for i in range(1, 20):
    print(f"{i} is Prime : {is_prime(i)}")
