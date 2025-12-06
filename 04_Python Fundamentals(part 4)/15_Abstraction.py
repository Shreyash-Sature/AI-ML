"""
Abstraction : Hiding internal details and showing only essential features.

Synatx :
Python supports abstraction through the Abstract Base Class (ABC) and abstract methods.
To implement abstraction, we use:

from abc import ABC

"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self): #abstract method
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Mow..")

lion = Lion()  #created object of Lion class (no argument is passed)
lion.make_sound()  #calling method 

cow = Cow()
cow.make_sound()