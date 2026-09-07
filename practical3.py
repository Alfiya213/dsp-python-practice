# Aim: To perform various operations on Python lists
# and use built-in list functions.

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("Sliced List:", numbers[1:4])

# Adding an element
numbers.append(60)
print("After append():", numbers)

# Inserting an element
numbers.insert(2, 25)
print("After insert():", numbers)

# Removing an element
numbers.remove(25)
print("After remove():", numbers)

# Removing last element
numbers.pop()
print("After pop():", numbers)

# Finding length
print("Length of List:", len(numbers))

# Finding maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Finding sum
print("Sum:", sum(numbers))

# Sorting the list
numbers.sort()
print("After sort():", numbers)

# Reversing the list
numbers.reverse()
print("After reverse():", numbers)

# Counting an element
print("Count of 20:", numbers.count(20))

# Finding index
print("Index of 30:", numbers.index(30))
