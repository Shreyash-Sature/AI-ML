"""
Create a BankAccount class with attributes, acc_number, owner_name and  balance.
Add methods to deposit, withdraw and check balance.
"""

class BankAccount:
    def __init__(self,acc_number, owner_name,balance):
        self.acc_number = acc_number
        self.owner_name = owner_name
        self._balance = balance

    def deposit(self,deposit_amnt):
        self.deposit_amnt = deposit_amnt
        self._balance += deposit_amnt

        print(f"{self.deposit_amnt} Rs deposited successfully!! and current balance is {self._balance} rs.")

    def withdraw(self,withdraw_amnt):
        self.withdraw_amnt = withdraw_amnt
        self._balance -= withdraw_amnt

        print(f"{self.withdraw_amnt} Rs withdrawed, Current balance is {self._balance} rs.")

    def get_balance(self):
        return self._balance
    
cust1 = BankAccount("98876362912","Shreyash",50000)

print(cust1.get_balance())

cust1.deposit(1500)
cust1.withdraw(600)