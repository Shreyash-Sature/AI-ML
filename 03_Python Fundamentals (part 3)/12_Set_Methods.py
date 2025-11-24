# 1. add()
numbers = {1, 2}
numbers.add(3)
print(numbers) # {1, 2, 3}

# 2. update()
fruits = {"apple", "banana"}
fruits.update(["grapes", "mango"])
print(fruits)

# 3. remove()
marks = {10, 20, 30}
marks.remove(20)
print(marks)

# 4. discard()
cities = {"Pune", "Delhi", "Mumbai"}
cities.discard("Goa")   # No error if not found

# 5. pop()
colors = {"red", "blue", "green"}
removed = colors.pop()
print(removed, colors)

# 6. clear()
items = {1, 2, 3}
items.clear()
print(items)   # set()

# 7. union()
setA = {1, 2}
setB = {2, 3}
result = setA.union(setB)
print(result)   # {1, 2, 3}


# 8. intersection()
x = {1, 2, 3}
y = {2, 3, 4}
print(x.intersection(y))   # {2, 3}

# 9. difference()
python_set = {1, 2, 3, 4}
java_set = {3, 4}
print(python_set.difference(java_set))   # {1, 2}

# 10. symmetric_difference()
even = {2, 4, 6}
odd = {1, 3, 5, 6}
print(even.symmetric_difference(odd))   # {1, 2, 3, 4, 5}

