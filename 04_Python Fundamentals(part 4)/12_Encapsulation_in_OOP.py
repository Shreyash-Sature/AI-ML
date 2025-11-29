#Encapsulation : Wrapping data + methods into a single unit (class) and restricting direct access to data.
"""
Three levels of data hiding:
i)Public : Attributes that are accessible inside and outide of class
Syntax :(variable)

ii)Protected: accessible in class and subclass
Syntax :(_variable)

iii)Private: accessible only in class
Syntax :(__variable)
getters and setters(functions) are used to access and update private variables safely
"""

class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_info(self):
        print(f"Name of account holder is {self.name} and acc balance is {self.__balance}")

cust1 = Bank("Shreyash",111_01_00_000)
cust2 = Bank("Shreya",1_00_000)
cust1.get_info()
cust2.get_info()