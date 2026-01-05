"""
Exception Handling : 
                     a mechanism to handle runtime errors so that the 
                     normal flow of the program does not stop abruptly.

visit : https://www.w3schools.com/python/python_ref_exceptions.asp
for builtin exceptions in python

Keywords Used in Exception Handling :
| Keyword   | Purpose                       |
| --------- | ----------------------------- |
| `try`     | Code that may cause exception |
| `except`  | Handles exception             |
| `else`    | Runs if no exception occurs   |
| `finally` | Always executed               |
| `raise`   | Manually raise exception      |

Syntax for try-except-else :

try:
     operation/code

except exception:
     code after exception occurs

else:
     code if exception not occurs
"""

try:
    x =int(input())
    ans = 10/x

except ZeroDivisionError:
    print("Division by 0 is not possible.")
except ValueError:
    print("Invalid input, enter a number.")

else:
    print(f"ans = {ans}")

finally:
    print("End of program.")
