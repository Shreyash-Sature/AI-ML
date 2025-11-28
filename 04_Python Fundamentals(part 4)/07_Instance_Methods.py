"""
Methods : Instance method
          Class method
          Static method
"""
#Instance Method : 
#Its first parameter is (self)
""" It can access Instance attributes/variables, Class variables and call other methods in same class """

class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_info(self):  #Instance Method : can access class and instance attributes/variables
        print(f"This Laptop has {l1.RAM} RAM and {l1.storage} {l1.storage_type}")

l1 = Laptop("8GB","256GB")
l2 = Laptop("16GB","512GB")

l1.get_info()

