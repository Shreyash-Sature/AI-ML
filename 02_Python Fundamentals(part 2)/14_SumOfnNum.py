# sum of n numbers using range function

#Print sum of first n natural numbers

n = int(input("Enter the number :"))
sum =0
for var in range(1,n+1):
    sum = sum + var
    
    
print("Sum of first",n,"natural numbers is :",sum)