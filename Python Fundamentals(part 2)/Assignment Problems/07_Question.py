"""Design a program to continuosly nput a number  from user and print if it is positive or negative until the user enter quit"""

def func():
    while(1>0):
        n = (input("Enter the number to check it is positive or negative :"))
        if(str(n)=='quit'):
            print("Program Stopped")
            break
        num = int(n)
        if(num >0):
            print("Number is positive.")
        elif(num<0):
            print("Number is negative.")
        elif(num ==0):
            print("Number is 0.")
        
func()



