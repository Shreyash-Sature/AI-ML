"""
Write a function that prints the digits of a number ,n

"""


# def func(n):
#     for i in range(len(str(n))):
#         last_dig = n % 10
#         print(int(last_dig))
#         n = n /10
# func(n)


n = int(input("Enter number :"))

def func(n):
    for i in range(len(str(n))):
        dig = n // (10 ** (len(str(n)) - 1))      
        n = n - (dig * (10 ** (len(str(n)) - 1))) 
        print(dig)

func(n)
