"""Write a function is_prime(n) that returns true if n is a prime number and flase otherwise using a loop."""

def is_prime(n):
    k = int((n**(1/2))+1)
    for i in range(2,k+2,1):
        if(n%i==0):
            print("Not Prime")
            break
            
        elif(n%i!=0):
            print("Is Prime"

n = int(input("Enter the number :"))
is_prime(n)