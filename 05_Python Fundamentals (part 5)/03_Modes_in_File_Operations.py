"""
Modes :
     r : opens file for reading (default)
         pointer at beggining

     w : open file for writing
         (first truncates/clears file and overwrite )

     x : creates new file and open for writing 
         throws error if file already exista
         (doesnt support overwriting for existing file )
    
     a : opens file for writing , appends data at end

     r+ : Reads and writes
          File must exist
          Pointer at beginning
          (writes data at the beginnig of file)

     w+ : reads and writes
          Existing data is deleted
          (and starts to write from beginning)

     a+ : reads and appends
          pointer at end (appends write at the end of file )
          creats new file if doesnt exist

     rb : Reads binary files (images, videos, pdf)

     wb : Writes binary files
"""

#Reading Mode 
f = open("data.txt","r")
data = f.read()
print(data)
f.close()

#Writing mode 
f= open("data.txt", "w")
data = f.write("Hellow\nMy name is Shreyash\nWhats your name?")
f.close()

#Exclusive Writing
f= open("data2.txt","x")
data = f.write("This is second file.")
f.close()

#Append
f= open("data2.txt", "a")
data = f.write("\nAppending data...")
f.close()

f=open("data.txt","r+")
data = f.read()
print(data)
f.close()

f = open("data.txt","w+")
data = f.read()
print(data)
f.close()