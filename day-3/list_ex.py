list_a = []
list_b = list()
list_c = [10, 20, 30, 40, 50]

print(type(list_a))
print(type(list_b))
print(type(list_c))

list_d = list_c[:4]
print(dir(list_a))
print("List d : {list_d}")
list_e = list_c.reverse()
print(list_e)  # None, bcz reverse fn reverse the list in-place
print(list_c)

list_a.append(10)
list_a.append(20)
list_a.append(30)
list_a.insert(3, 40)
print(" List a :  {list_a}")


list_b.extend(list_a)
print(f"List b after extending it with list a : {list_b}")

list_a.append(60)
print(f"List a after apending 60 {list_a}")
print(f"Does it affect list b : {list_b}")
