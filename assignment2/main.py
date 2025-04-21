# 1. Arithmetic Operators
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus (remainder): 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor Division: 3

# 2. Assignment Operators

x = 5

x += 3  # x = x + 3
print(x)  # 8

x -= 2  # x = x - 2
print(x)  # 6

x *= 2
print(x)  # 12

x /= 3
print(x)  # 4.0

x %= 3
print(x)  # 1.0

x **= 2
print(x)  # 1.0

x //= 2
print(x)  # 0.0

# 3. Logical Operators

a = True
b = False

print(a and b) # False
print(a or b)  # True
print(not a)   # False

# 4. Comparison Operators
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

# 5. Bitwise Operators
a = 5      # 0101
b = 3      # 0011

print(a & b)  # AND: 1
print(a | b)  # OR: 7
print(a ^ b)  # XOR: 6
print(~a)     # NOT: -6
print(a << 1) # Left shift: 10
print(a >> 1) # Right shift: 2

# 6. Membership Operators
my_list = [1, 2, 3]

print(2 in my_list)      # True
print(4 not in my_list)  # True

# 7. Identity Operators
x = [1, 2]
y = [1, 2]
z = x

print(x is y)      # False (different objects)
print(x is z)      # True (same object)
print(x is not y)  # True
