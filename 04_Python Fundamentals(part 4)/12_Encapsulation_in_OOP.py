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

class BankAccount:
    def __init__(self,name,balance):
        self.name = name  #public attribute
        self.__balance = balance   #private attribute - data mangling

    def get_balance(self): #getter function
        return self.__balance
    
    def set_balance(self,newBalance): #setter function to update the private attribute
        self.__balance = newBalance
        
    
    
acc1 = BankAccount("Shreyash",100000)
acc2 = BankAccount("Shreya", 1000)

print(acc1.name, acc1.get_balance())

acc1.set_balance(200000) #to update the private attribute (balance)
print(acc1.name, acc1.get_balance())
