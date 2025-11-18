"""Write a function that takes two integers as input and prints all even numbers between them"""

def even_num(a,b):
    for i in range(a,b+1,1):
        if(i%2==0):
            print(i)

even_num(4,26)