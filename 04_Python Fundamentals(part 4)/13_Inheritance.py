"""
Inheritance : Allows one class to acquire the properties (variables) and 
              behaviors (methods) of another class.

 -This helps in code reusability, reducing redundancy, and 
            creating hierarchical relationships between classes.

-while creating child class write parent class name in parenthesis after child class name

-Syntax :
class PARENT:
    # parent class code

class Child (PARENT):
    # child class inherits Parent

                 
"""

"""
Protected Attributes:
-Meant to be accessed only within the class and its subclasses
-Declared using one underscore _ before the attribute name

Private Attributes:
-Accessible only inside the class
-Declared using two underscores __ before the attribute

"""

class Employee:                  #Parent class
    start_time = "10am"
    end_time = "5pm"     #attributes can be accessed anywhere 

    def change_time(self,new_start_time): #method to update the start time
        self.start_time = new_start_time

class Teachers(Employee):  #child class that inherits parents class
    def __init__(self,subject):
        self.subject = subject

class Admin_Staff(Employee):   #another child class
    def __init__(self, role):
        self.role = role
    
teacher1 = Teachers("Maths")
print(teacher1.start_time, teacher1.subject, teacher1.end_time)#prints time before updation
teacher1.change_time("11am")
print(teacher1.start_time, teacher1.subject, teacher1.end_time) #prints time after updation

staff1 = Admin_Staff("Manager")
print(staff1.start_time, staff1.role)

