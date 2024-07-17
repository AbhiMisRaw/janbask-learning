from abc import ABC, abstractmethod


class Professional(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def quote(self, q):
        pass


class Doctor(Professional):

    def __init__(self, name, age):
        super().__init__(name, age)

    def quote(self, q):
        print("\n+++++++++++++++ QUOTE +++++++++++++++")
        print("We'r Doctors")
        print(f"and My Dailog is '{q}'")
        print("========================================")


class SoftwareEngineer(Professional):

    def __init__(self, name, age):
        super().__init__(name, age)

    def quote(self, q):
        print("We are Software Engineers")
        print("We built Software")
        print(f"We say {q}")


doc = Doctor("Arun Gupta", 34)
eng = SoftwareEngineer("Abhishek Mishra", 34)

print(dir(doc))
doc.quote("We save life")

