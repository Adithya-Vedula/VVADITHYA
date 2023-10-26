print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex23.py" + " ============")

#made by adithya

# Input a list
original_list = [8, -5, 0, 3, -2, 1, -4, 7, -7, 3]

# Initialize empty lists for positive and negative elements
positive_elements = []
negative_elements = []

# Separate positive and negative elements
for num in original_list:
    if num >= 0:
        positive_elements.append(num)
    else:
        negative_elements.append(num)

# Combine negative elements followed by positive elements
resultant_list = negative_elements + positive_elements

print("Original list:", original_list)
print("Resultant list:", resultant_list)

#made by adithya
