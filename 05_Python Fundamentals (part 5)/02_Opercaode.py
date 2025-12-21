f = open("data.txt" ,"r")

data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()

f = open("data.txt","w")
f.write("How are you ?")

f.close()

f=open("data.txt","r")
data = f.read()

