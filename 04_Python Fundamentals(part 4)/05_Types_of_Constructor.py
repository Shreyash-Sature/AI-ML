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

#Non-parameterized Constructor
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

