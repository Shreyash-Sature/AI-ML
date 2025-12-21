"""
Create a program that :
i) Opens a file "log.txt" in append mode
ii) Adds a new log entry (like"Program run successfully")
iii) opens the file in read mode and prints all logs
"""

with open("log.txt", "a") as f:
    data = f.write("\nProgram Run Successfully")

with open("log.txt","r") as f:
    data = f.read()
    print(data)