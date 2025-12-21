"""
Create a program that:
i) Has a list of numbers: [5,10,15,20,25]
ii) Uses a list comprehension to create a new list with only numbers greater than 15
iii) Prints the new list
"""

list = []
list = [5*i for i in range(1,6)]
print(list)
list = [num for num in list if num >15]
print("Numbers greater than 15 are :",list)