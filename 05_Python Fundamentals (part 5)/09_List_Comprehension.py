"""
List Comprehension in Python :
a concise and readable way to create lists in Python using a single line of code.

Syntax :

new_list = [EXPRESSION for ITEM in ITERABLE if CONDITION]

expression → what to add to list
item → variable
iterable → list, tuple, range, string, etc.
condition → optional filter

"""
list =[]
for i in range(6):
    list.append(i*i)
print(list)


list = [i*i for i in range(6)]
print(list)


list = [i*i for i in range(9) if i%2!=0]
print(list)

nums =[-3,2,4,6,5,1,-8]
list = [0 if value<0 else value for value in nums]
print(list)

words=["shreyash","hellow","world"]
words=[word.upper() for word in words]
print(words)