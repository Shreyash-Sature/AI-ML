""" Functions : Blocks of Statements that performs specific tasks
_____________________________________________________________________________________________
-Function Definition in Python:
Function definition means creating a function — giving it a name, parameters, and writing the code it should execute.

Syntax:

def function_name(parameters):
    # code block
_____________________________________________________________________________________________

-Function Call in Python

Function call means using the function — telling Python to run the code inside the function.

Syntax:
function_name(arguments)
_____________________________________________________________________________________________

"""
# def hello():
#     print("Hello how are you?")

# hello()


#_____________________________________________________________________________________________

#function definition

def sum(a,b):#parameters 
    s = a + b
    return s

#function call
ans = sum(4,5)
print(ans)
