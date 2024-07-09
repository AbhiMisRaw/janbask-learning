while True:
    num = int(input("Enter any Number : "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    cond = input("You want more table if yes press 'Y' else 'N' ")
    if cond == "N":
        print("Thank You!")
        break
else:
    print("Some Error Occured!")
