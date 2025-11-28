"""
1) Class atributes : belongs to class 
2) Instance attribute : belongs to object
"""

class Student:
    clg_name = "DYPIT"     #class atribute

    def __init__(self,name,age):
        self.name = name           #instance attributes
        self.age = age

stud1 = Student("Shreyash",20)
print(stud1.clg_name)
