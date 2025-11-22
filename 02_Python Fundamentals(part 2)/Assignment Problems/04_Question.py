"""Write a function to return the count the number of digits in a number,n"""
n = int(input("Enter the number : "))

def num (n):
    count = 0
    while(n>0):
        
        n = int(n /10)
        count = count +1
    return count
    
ans = num(n)
print("Number of digits in given number is :", ans)

        
