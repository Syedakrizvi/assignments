# Control Flow Example in Python
# 1. if example
score = 85

if score > 80:
    print("Great job!")

# 2. if with else example
is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy the sunshine!")

#  3. if, elif, and else
marks = 70

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# Nested if Example 

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the movie theater.")
    else:
        print("You need a ticket to enter.")
else:
    print("You're too young to enter.")


    # LOOPS Examples

# 1. for Loop with else(no break)
for i in range(5):
    print(i)
else:
    print("Loop finished without a break.")

#  2. for Loop with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not print because of break.")

# 3. while Loop Example
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# 4. Controlling a Loop (with continue)

for i in range(5):
    if i == 2:
        continue  # Skip number 2
    print(i)

# 5. Nested Loop Example

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
