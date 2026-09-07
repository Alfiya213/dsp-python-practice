# Aim: Write a program to understand Python building blocks,
# data types, and basic input-output operations by creating
# a student data system.

print("===== STUDENT DATA SYSTEM =====")

# Taking input from the user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
branch = input("Enter branch: ")
marks = float(input("Enter marks: "))

# Displaying student data
print("\n===== STUDENT DETAILS =====")
print("Name      :", name)
print("Roll No.  :", roll_no)
print("Age       :", age)
print("Branch    :", branch)
print("Marks     :", marks)

# Displaying data types
print("\n===== DATA TYPES =====")
print("Name data type     :", type(name))
print("Roll No. data type :", type(roll_no))
print("Age data type      :", type(age))
print("Branch data type   :", type(branch))
print("Marks data type    :", type(marks))

print("\nStudent data entered successfully!")
