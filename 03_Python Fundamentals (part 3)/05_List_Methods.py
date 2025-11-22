# 1. append() – Adds an element at the end
nums = [1, 2, 3]
nums.append(4)
print(nums)      # [1, 2, 3, 4]

# 2. insert() – Inserts at a specific index
nums = [1, 2, 3]
nums.insert(1, 99)
print(nums)      # [1, 99, 2, 3]

# 3. extend() – Adds multiple items from another list
nums = [1, 2]
more = [3, 4]
nums.extend(more)
print(nums)      # [1, 2, 3, 4]

# 4. remove() – Removes the first occurrence of a value
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)      # [1, 3, 2]


# Error if value not found.

# 5. pop() – Removes element by index (default: last)
nums = [10, 20, 30]
nums.pop()        # removes 30
nums.pop(0)       # removes 10
print(nums)       # [20]

# 6. clear() – Removes all elements
nums = [1, 2, 3]
nums.clear()
print(nums)       # []

# 7. sort() – Sorts the list
nums = [4, 1, 3, 2]
nums.sort()
print(nums)       # [1, 2, 3, 4]

nums.sort(reverse=True)
print(nums)       # [4, 3, 2, 1]

# 8. reverse() – Reverses the list
nums = [1, 2, 3]
nums.reverse()
print(nums)       # [3, 2, 1]

# 9. count() – Counts occurrences of a value
nums = [1, 2, 2, 3]
print(nums.count(2))     # 2

# 10. index() – Returns index of first occurrence
nums = [5, 10, 15]
print(nums.index(10))    # 1

