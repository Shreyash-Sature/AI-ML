"""
JSON (Java script object notation) : 

json.dumps(): Python → JSON (String)
json.loads() : JSON(Strings) → Python


"""
import json


#for strings
json_str = '{"name" : "Shreyash", "isStudent" : true}'
py_obj = json.loads(json_str)   #JSON to Python (Strings)
print(py_obj, type(py_obj))

py_obj = {
    "name " : "Shreyash",
    "isStudent" : True
} 
json_obj = json.dumps(py_obj)     #Python to JSON (Strings)
print(json_obj, type(json_obj))


#for files 
#loads JSON info to Python
with open("10_data.json","r") as f:
    py_obj = json.load(f)

    print(py_obj,type(py_obj))


#dumps Python info to JSON file

data ={
    "name" : "Shreyash",
    "isStudent":True,
    "age" : 21
}

with open("10_data.json","w") as f:
    json.dump(data,f, indent=4, sort_keys=True)