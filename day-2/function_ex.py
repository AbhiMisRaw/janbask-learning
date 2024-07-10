def find(target, args):
    for i in args:
        if i is target:
            return True

    return False


def find_max(args):
    if args is None:
        raise Exception("Please pass Collection")
    max = args[0]
    for i in args:
        if max < i:
            max = i

    return max


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 18
print(f"{target} present in List {list_a} : {find(target,list_a)}")

print(f"Max number in list {list_a} : {find_max(list_a)} ")
