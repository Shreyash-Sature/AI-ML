"""Letʼs create a Simple Calculator that performs arithmatic operations. Create a function calculator(a,b,operation) that performs addition, substration , multiplication
based on operation parameters"""


def calculator(a,b,operation):
    if(operation == '+'):
        ans = a + b
        print ("Sum = ",ans)
    elif(operation == '-'):
        ans = a - b
        print ("Substraction = ",ans)
    elif(operation == '*'):
        ans = a * b
        print ("Multiplication = ",ans)
    elif(operation == '/'):
        ans = a / b
        print ("Division = ",ans)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
operation=(input("Enter the operation you have to perform:"))

calculator(a,b,operation)

    


