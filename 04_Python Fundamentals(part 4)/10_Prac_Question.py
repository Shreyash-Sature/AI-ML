"""
Design and create an online store for products (name and price)
Track total products begin created
Create a static method to calculate discount on each product based on a % parameter
"""

class Product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count +=1      #class variable hence Product.count 
    
    def get_info(self): #instance method
        print(f"Price of {self.name} is {self.price} Rs.")

    @classmethod
    def get_count(cls):
        print(f"Total number of products is {cls.count}.")

    @staticmethod
    def cal_discount(price,discount):
        print(f"Final price is {price - (discount*price/100)}")


p1 = Product("Laptop",70_000)
p2 = Product("Phone",25_000)
p3 = Product("Pen",10)
p4 = Product("Notebook",100)

p4.get_info()
Product.get_count()
p1.cal_discount(p1.price,10)