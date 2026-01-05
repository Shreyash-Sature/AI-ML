"""
"with" keyword in file handling : 
                                  It ensures that a resource (like a file) is 
                                  properly opened and closed, even if an error occurs.
Normally, we write:

f = open("data.txt", "r")
print(f.read())
f.close()

If an error occurs before f.close(), the file remains open
Can cause memory leaks
"""

with open("data.txt","r") as f:
    print(f.read())

"""
File is automatically closed
Cleaner and safer
"""