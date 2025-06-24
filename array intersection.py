# Input size for both sets
n = int(input("Enter number of elements for each set: "))

# Read first set
set_one = set()
print("Enter elements for the first set:")
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    set_one.add(element)

# Read second set
set_two = set()
print("Enter elements for the second set:")
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    set_two.add(element)

# Calculate intersection
intersection = set_one & set_two  # or set_one.intersection(set_two)

# Print result
print("Intersection of the two sets is:", list(intersection))
