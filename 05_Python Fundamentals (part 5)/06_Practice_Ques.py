data = True

print("Enter the word to search : ")
word = input(str())
count =0
with open("data.txt","r") as f:
    while data:
        data = f.readline()
        count +=1
        if(word in data ):
            print(f"Word found at line number {count} ")
            break
    else :
        print("Word not found !")

    
