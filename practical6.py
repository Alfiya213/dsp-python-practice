# Aim: To perform array creation, indexing, slicing,
# reshaping, and mathematical operations using NumPy.

import numpy as np

# Array Creation
arr = np.array([10, 20, 30, 40, 50, 60])

print("----- ARRAY CREATION -----")
print("Array:", arr)

# Indexing
print("\n----- INDEXING -----")
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Last Element:", arr[-1])

# Slicing
print("\n----- SLICING -----")
print("Elements from index 1 to 4:", arr[1:5])
print("First three elements:", arr[:3])
print("Last three elements:", arr[-3:])

# Reshaping
print("\n----- RESHAPING -----")
matrix = arr.reshape(2, 3)
print("2 x 3 Matrix:")
print(matrix)

# Mathematical Operations
print("\n----- MATHEMATICAL OPERATIONS -----")
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
