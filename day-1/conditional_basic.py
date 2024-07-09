age = int(input("Please Enter Your age :"))

if age < 18:
    print("Sorry, You are not eligible to vote")
else:
    x = input("Press 'Y' if you've Voter ID Card else 'N' : ")
    if x == "Y":
        print("Congrats, You are eligible to vote")
    else:
        print("Please apply for the Voter Id Card")
