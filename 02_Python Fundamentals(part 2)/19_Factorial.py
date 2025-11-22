"""Write a function to calculate the factorial of a function"""

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return fact  
n = int(input("Enter the number to get the factorial :"))
print("Factorial is :",factorial(n))  

    
        
    

