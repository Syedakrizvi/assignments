# Example of Set in python
# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Printing the set
print("Original set:", numbers)

# Adding an element to the set
numbers.add(6)
print("After adding 6:", numbers)

# Adding a duplicate (won't change the set)
numbers.add(3)
print("After trying to add duplicate 3:", numbers)

# Removing an element
numbers.remove(2)
print("After removing 2:", numbers)

# Checking membership
print("Is 4 in the set?", 4 in numbers)
print("Is 10 in the set?", 10 in numbers)

# Looping through the set
print("Elements in the set:")
for num in numbers:
    print("-", num)

# Set operations
even = {2, 4, 6, 8}
print("Union:", numbers.union(even))
print("Intersection:", numbers.intersection(even))
print("Difference:", numbers.difference(even))


                      # Frozen_set examples

# Creating a normal set
normal_set = {"apple", "banana", "cherry"}

# Creating a frozenset from the normal set
frozen_set = frozenset(normal_set)

# Printing the frozenset
print("Frozen set:", frozen_set)

# Trying to add an element (will raise an error)
try:
    frozen_set.add("orange")
except AttributeError as e:
    print("Error:", e)

# Trying to remove an element (will also raise an error)
try:
    frozen_set.remove("banana")
except AttributeError as e:
    print("Error:", e)

# You can still perform set operations
another_set = {"banana", "mango", "apple"}
intersection = frozen_set.intersection(another_set)
print("Common elements (intersection):", intersection)
