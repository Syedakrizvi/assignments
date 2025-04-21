# Example of list
# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "mango"]

# Printing the entire list
print("Fruits list:", fruits)

# Accessing elements in the list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding a new item to the list
fruits.append("orange")
print("Updated list after append:", fruits)

# Removing an item from the list
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Looping through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

                           # Tuple Example
# Creating a tuple of colors
colors = ("red", "green", "blue")

# Printing the entire tuple
print("Colors tuple:", colors)

# Accessing elements in the tuple
print("First color:", colors[0])
print("Last color:", colors[-1])

# Looping through a tuple
print("All colors:")
for color in colors:
    print("-", color)

# Checking the length of the tuple
print("Number of colors:", len(colors))

# Trying to modify a tuple (this will raise an error)
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)
                            #    Dictionaries Example
                            
# Creating a dictionary with some person details
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Printing the entire dictionary
print("Person dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Adding a new key-value pair
person["profession"] = "Engineer"
print("Updated dictionary:", person)

# Modifying a value
person["age"] = 26
print("Dictionary after updating age:", person)

# Removing a key-value pair
del person["city"]
print("Dictionary after deleting city:", person)

# Looping through dictionary keys and values
print("All key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
