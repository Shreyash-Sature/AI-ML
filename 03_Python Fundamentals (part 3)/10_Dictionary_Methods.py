info = {
    "name" : "Shreyash Sature",
    "Address" : "Pandharpur",
    "cgpa" : 8.7,
    "Subjects" : ["DBMS","CNS","SPOS","HCI","TOC"],
    3.14 : "PI"
}

# info.keys() => returns all keys
print(info.keys())

# info.values => returs all values
print(info.values())

print(info.items()) #retues key value pairs 

print(info.get("cgpa")) #=> returs value according to key

info.update({
    "cgpa2" : 9.2
})
print(info)
 