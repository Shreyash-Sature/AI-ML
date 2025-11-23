"""
Dictionary : An Unordered , Mutable collection of KEY-VALUE PAIRS.
- use unique key for each value 
-key must be immutable (str, int , etc)

Synatx :

dict_name = {
    key : value,
    key1 : value1,
    }
"""

info = {
    "name" : "Shreyash Sature",
    "Address" : "Pandharpur",
    "cgpa" : 8.7,
    "Subjects" : ["DBMS","CNS","SPOS","HCI","TOC"],
    3.14 : "PI"
}

print(info)
print(type(info))

#To accesss particular key value
print(info["name"])

#Update Dictionary
info["cgpa"] = 8.07
print(info["cgpa"])