class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark():
        print("Woof Woof")

    def intro(self):
        return "{" + f"name:{self.name}, age:{self.age}" + "}"


tommy = Dog("Tommy", 4)

tommy.bark()

print(tommy.intro())

