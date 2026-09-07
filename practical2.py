# Aim: To implement arithmetic, relational, logical,
# bitwise, and assignment operators in Python.

a = 10
b = 5

# Arithmetic Operators
print("----- Arithmetic Operators -----")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)
print("Floor Division :", a // b)

# Relational Operators
print("\n----- Relational Operators -----")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
x = True
y = False

print("\n----- Logical Operators -----")
print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

# Bitwise Operators
print("\n----- Bitwise Operators -----")
print("a & b  :", a & b)
print("a | b  :", a | b)
print("a ^ b  :", a ^ b)
print("~a     :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)

# Assignment Operators
print("\n----- Assignment Operators -----")
c = 10
print("Initial c :", c)

c += 5
print("c += 5    :", c)

c -= 3
print("c -= 3    :", c)

c *= 2
print("c *= 2    :", c)

c /= 2
print("c /= 2    :", c)

c %= 4
print("c %= 4    :", c)
