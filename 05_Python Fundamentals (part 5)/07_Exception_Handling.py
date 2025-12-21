"""
Exception Handling : 
                     a mechanism to handle runtime errors so that the 
                     normal flow of the program does not stop abruptly.

Keywords Used in Exception Handling :
| Keyword   | Purpose                       |
| --------- | ----------------------------- |
| `try`     | Code that may cause exception |
| `except`  | Handles exception             |
| `else`    | Runs if no exception occurs   |
| `finally` | Always executed               |
| `raise`   | Manually raise exception      |

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
