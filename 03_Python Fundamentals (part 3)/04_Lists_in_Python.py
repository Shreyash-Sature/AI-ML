"""
-Lists: An ordered, changeable (mutable), and indexed collection of items.

-Can store same type or different types of values

Synatx : my_list = [10, 20, 30, "hello", 5.5]

-Lists are muttable (we can update lists after creation)

"""
marks =[98,87,90,69,"abc",92]
print(len(marks))
print(marks[2])
print(marks)

#update string
marks[2] = 93
print (marks[2])

"""
Slicing in Lists : """
print(marks[2:5])