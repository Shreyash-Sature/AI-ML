"""
Polymorphism : "many forms" — the same function or method behaves differently in 
               different situations.

1)Method Overloading : (Same method name, different parameters)

2)Method Overriding : Redefining parent class function in child class.
Occurs when a child class has a method with the same name as the parent method,
 but with modified behavior.
"""

class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

t1= Teacher()
t1.get_designation()

