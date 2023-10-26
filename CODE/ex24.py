print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex24.py" + " ============")

#made by adithya

# Input a list
L = [1, 2, 1, 3, 4, 3, 4, 3, 2, 4, 5, 6]

# Initialize empty lists for unique and duplicate elements
unique_elements = []
duplicate_elements = []

# Iterate through the list to find unique and duplicate elements
for item in L:
    if L.count(item) > 1 and item not in duplicate_elements:
        duplicate_elements.append(item)
    elif L.count(item) == 1 and item not in unique_elements:
        unique_elements.append(item)

# Output the results
print("Duplicated elements of the list are:", duplicate_elements)
print("Unique elements in the list are:", unique_elements)
