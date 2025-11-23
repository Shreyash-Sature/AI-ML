"""
Tuples : An ordered, immutable collection of items.
-Allow duplicates elements
-Heterogenes.

Syntax : tuple_name = (el1, el2, el3)

"""

# tup = (12,'asd',32)
# print(tup)

tup = (1,2,3,4,5)

#indexing and slicing
print(tup[2])
print(tup[1:4])

#Loops on tuple
sum =0
for var in tup :
    sum += var
print(f"Sum of elements in tuple is {sum} .")


