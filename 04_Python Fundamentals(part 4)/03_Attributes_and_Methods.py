"""
Atributes : variables inside a class that store data about an object.
"""
class Student:
    name = "Shreyash"
    age = 20
    branch = "Computer Science"

"""
here (name, age, branch) → attributes (properties)
They describe the data of each student.
"""

"""
Methods : These are functions inside a class that define what the object can do.

"""
class Student:
    name = "Shreyash"
    age = 20
    branch = "Computer Science"

    def study(self):
        print(self.name, "is studying.")

    def give_exam(self):
        print(self.name, "is giving exam.")

"""
Here,
study()
give_exam()
are methods (behaviours) because they show what the student can do."""

