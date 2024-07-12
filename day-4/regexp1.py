# re.search() : returns true/false depending on weather string matches the string or not

# re.findall() : extacted the actual string after matching reg-ex

import re

number = "My 2 fav numbers are 7 and 45"

y = re.findall("[0-9]+", number)

z = re.findall("[0-9][0-9]+", number)  # 45

print(f"{y} : {type(y)}")

intro = "My name is Abhishek Mishra, I am from Kanpur"

# now i want to extract only helping verb

verbs = re.findall("[ai].+?", intro)
print(verbs)
