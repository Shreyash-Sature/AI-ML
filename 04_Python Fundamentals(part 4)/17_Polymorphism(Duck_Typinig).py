"""
Duck Typing : the type or class of an object is not important —
              the behavior (methods/properties) matters.
"""

class Teacher:
    def get_designation(self):
        print("Designation = Teacher")

class Accountant:             # No inheritance (no relation between two classes)
    def get_designation(self):
        print("Designation = Accountant")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()