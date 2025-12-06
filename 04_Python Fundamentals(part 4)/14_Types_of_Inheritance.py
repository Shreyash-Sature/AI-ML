"""
| Type of Inheritance | Diagram                 | Example Structure               |
| ------------------- | ----------------------- | ------------------------------- |
| Single              | A → B                   | One parent → One child          |
| Multilevel          | A → B → C               | Grandparent → Parent → Child    |
| Multiple            | A ← C → B               | Child inherits multiple parents |
| Hierarchical        | Parent → Child1, Child2 | One parent → Many children      |
| Hybrid              | Combination             | Mix of hierarchical + multiple  |

Types of INheritance :

1) Single level inheritance : A child class inherits from one parent class.(only one child class and one parent class inheritance ,
                              no further inheritance.)

"""
print("Single Level inheritance : ")
class Employee:
    start_time = "10am"
    end_time = "5pm"

    def __init__(self,new_start_time):
        self.start_time = new_start_time

class Admin_Staff(Employee):
    def __init__(self,role):
        self.role = role

staff1 = Admin_Staff("Manager")
print(staff1.start_time, staff1.role)

"""
2)Multilevel inheritance : Inheritance occurs in a chain (A → B → C).
     

-super() keyword : used inside a child class to call the parent class constructor or methods.
"""
print("2) Multilevel Inheritance :")
class Employee:
    start_time = "10am"
    end_time = "5pm"

    def __init__(self,new_start_time):
        self.start_time = new_start_time

class Admin_Staff(Employee):
    def __init__(self,role):
        self.role = role
    
class Accountant(Admin_Staff):
    def __init__(self,salary,role):
        super().__init__(role)   #super() keyword used inside a child class to call the parent class constructor or methods.
        self.salary = salary

staff1 = Accountant(50000, "Manager")
print(staff1.start_time, staff1.salary, staff1.role)


"""
3)Multiple Inheritance : A child class inherits from more than one parent class.
  
"""
print("3)Multiple Inheritance : ")
class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class Teacher_Assistant(Teacher, Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)     # to call constructor of 1st class
        Student.__init__(self,gpa)       # to call constructor of 2nd class
        self.name = name

stud1 = Teacher_Assistant(20000, 9.1, "Sumit ")
print(stud1.name,stud1.gpa,stud1.salary)

