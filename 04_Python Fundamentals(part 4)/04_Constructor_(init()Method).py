"""
A constructor is a special method that is automatically called when an object is created.

To assign property/attribute values when object is created
To avoid manually setting attributes later
To give each object its own data

Syntax : 
def __init__(self, parameters):
    # initialize attributes

self refers to the current object

"""
class Student :
    def __init__(self,name,age ,branch): #constructor
        self.name = name                 
        self.age = age               #attributes
        self.branch = branch

stud1 = Student("Shreyash",20,"Computer")
stud2 = Student("Kaalu",20,"IT")

print(f"Name of student is {stud1.name} and Branch of student is {stud1.branch}." )
print(stud2.name, stud2.age)
