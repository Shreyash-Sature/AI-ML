# Default Constructor 
class Student:
    def __init__(self):
        print("Default Constructor Called")

s = Student()   # object creation


# Parameterized Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Rahul", 20)
print(s.name, s.age)
