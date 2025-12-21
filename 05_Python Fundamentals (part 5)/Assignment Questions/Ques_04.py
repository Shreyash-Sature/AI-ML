"""
Create a Python dictionary of 3 cities and their populations. 
Save it to "cities.json".
1. Then load JSON and print each city and its population.
2. ask the user for a new city and its population - update this info in the json file.

"""
import json
cities ={
    "Pune" : 2_367_541,
    "Mumbai" : 5_324_321,
    "Pandharpur": 243_987
}

with open("cities.txt","w") as f:
    json.dump(cities,f,indent=4)

