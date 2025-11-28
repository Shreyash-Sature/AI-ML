"""
Class Method : 
Its first parameter is (cls)

can only access Class attributes and not Instance attribute

use class decorator

"""
class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod #<- this is class decorator that changes behaviour of method and written above method
    def get_storage_type(cls):  # Class method : only access class attributes/variables
        print(f"Storage type of this laptop is {cls.storage_type}.")

    def get_info(self):  #Instance Method : can access class and instance attributes/variables
        print(f"This Laptop has {l1.RAM} RAM and {l1.storage} {l1.storage_type}.")


L1 = Laptop("16GB","512GB") #object 

L1.get_storage_type()