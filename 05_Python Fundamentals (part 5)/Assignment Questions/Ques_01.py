"""
Create a program that :
i) opens file "names.txt" in write mode
ii) Writes 5 names (one per line) entered by the user
iii) Then opens the same file in read mode and prints all names

"""
with open("name.txt","w") as f:
    for i in range(5):
        names = input(f"Enter name {i+1} : ")
        f.write(names + "\n")

with open("name.txt", "r") as f:
    for i in range(5):
        data = f.readline()
        print(data)
