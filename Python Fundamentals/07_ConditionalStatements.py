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


#TRAFFIC LIGHT

color = input("Enter your color :")
if color == "Red":
    print("Stop")
elif color =="Yellow":
    print("Look")
elif color == "Green":
    print("Go")
else:
    print("Wrong color entered.")


#LOGIN INFO

    username = input("Enter username :")
    password = input("Enter your password :")

    if(username == "admin" and password == "pass"):
        print("Login Successful!")
    elif(username != "admin"):
        print("Incorrect Username !")
    else:
        print("Incorrect Password !")


#MULTIPLE OF 5

num = int(input("Enter number :"))
if(num % 5 ==0):
    print(num,"is divisible by 5.")
else:
    print("is not divisible by 5.")
