# Opening a file 
"""
Syntax : 

f = open("file_name", "mode")

mode : r(reading), w (write) ,etc
"""
f = open("data.txt", "r")


#Reading from file
"""
To read a file first open it into reading mode.
In reading mode you cant write file """
#read() – Reads entire file
f = open("data.txt", "r")
content = f.read()
print(content)


#readline() – Reads one line at a time
f = open("data.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1, line2)


#Writing to a File
"""
To write file first open file into write mode.
"""
f = open("data.txt", "w")
f.write("Hello World!\n")
f.write("How are you?.")


#Appending to a File
f = open("data.txt", "a")
f.write("\nNew line added.")


#Closing a File
f.close()

