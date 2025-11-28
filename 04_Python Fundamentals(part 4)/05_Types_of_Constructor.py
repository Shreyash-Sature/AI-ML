"""# Default Constructor 
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

"""
class Student :
    def __init__(self,name,age,cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa
    
stud1 = Student("Shreyash", 20,9.5)
print(f"{stud1.name} has cgpa of {stud1.get_cgpa()}")