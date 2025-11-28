"""
Static Fuctions:
"""
class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod 
    def get_storage_type(cls):  # Class method : only access class attributes/variables
        print(f"Storage type of this laptop is {cls.storage_type}.")

    def get_info(self):  #Instance Method : can access class and instance attributes/variables
        print(f"This Laptop has {l1.RAM} RAM and {l1.storage} {l1.storage_type}.")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price * (1-discount/100)
        print(f"Final price is {final_price}.")


L1 = Laptop("16GB","512GB") #object 

L1.calc_discount(40000,10) #calling Static method
