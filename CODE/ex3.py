print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex3.py" + " ============")
#made by adithya

# Input from the user
width = int(input("Enter the width of the building site in meters: "))
length = int(input("Enter the length of the building site in meters: "))

# Default gap of 4 meters
gap = 4

# Calculate the perimeter of the site
perimeter = 2 * (width + length)

# Add the gap to the perimeter
total_perimeter = perimeter - gap

# Calculate the number of panels needed (each panel is 1 meter long)
panels_needed = total_perimeter

# Print the result
print(f"The minimum number of full fence panels needed is: {panels_needed} panels")
