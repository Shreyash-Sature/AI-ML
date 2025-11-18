"""Types of Functions:

-Bult in functions : These are functions already provided by Python.
You can use them without defining them yourself.

Function	Purpose
print()	Displays output
len()	Returns length of string/list/etc.
type()	Shows the data type
input()	Takes input from user
max(), min()	Returns largest / smallest value
sum()	Adds all elements
sorted()	Returns a sorted list
range()	Generates a sequence of numbers


-User defined funtions  : These are functions that you create yourself using the def keyword."""

def add(a, b):
    result = a + b
    return result

print(add(10, 5))      # calling user-defined function