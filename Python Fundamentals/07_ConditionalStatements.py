"""
Conditional Statements
if, else, elif

"""
age = int(input("Enter your age :"))
if age>=18 :
    print("You can vote.")
    print("You can drive")
else:
    print("You can't vote.")

color = input("Enter your color :")
if color == "Red":
    print("Stop")
elif color =="Yellow":
    print("Look")
elif color == "Green":
    print("Go")
else:
    print("Wrong color entered.")