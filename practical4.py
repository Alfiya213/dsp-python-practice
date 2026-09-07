# Aim: To perform operations on tuple, set, and dictionary
# data structures.

# ---------------- TUPLE ----------------
print("----- TUPLE OPERATIONS -----")

my_tuple = (10, 20, 30, 40, 50)

print("Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])
print("Sliced Tuple:", my_tuple[1:4])
print("Length:", len(my_tuple))
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))


# ---------------- SET ----------------
print("\n----- SET OPERATIONS -----")

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

set1.add(50)
print("After add():", set1)

set1.remove(20)
print("After remove():", set1)


# ---------------- DICTIONARY ----------------
print("\n----- DICTIONARY OPERATIONS -----")

student = {
    "Name": "Alfiya",
    "Roll_No": 25,
    "Branch": "Data Science",
    "Marks": 85
}

print("Dictionary:", student)

# Accessing values
print("Student Name:", student["Name"])
print("Student Marks:", student["Marks"])

# Adding a new key-value pair
student["Age"] = 20
print("After adding Age:", student)

# Updating a value
student["Marks"] = 90
print("After updating Marks:", student)

# Removing an item
student.pop("Age")
print("After removing Age:", student)

# Built-in dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length:", len(student))
