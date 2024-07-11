d_a = {}
d_b = dict()

print(type(d_a))
print(type(d_b))
print(dir(d_a))

names = ["Abhi", "Mayank", "Killua", "Rohan", "Abhi", "Rahul", "Zhen", "Zhen", "Killua"]

for name in names:
    if name in d_a:
        d_a[name] += d_a[name]
    else:
        d_a[name] = 1

print(d_a)
# or

for name in names:
    d_b[name] = d_b.get(name, 0) + 1

print(d_b)
