print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex5.py" + " ============")
#made by adithya

# Input the length and breadth of the rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate the area of the rectangle
area = length * breadth

# Print the calculated area
print(f"The area of the rectangle is: {area} square units")

# Compare the area to a maximum value
maximum_area = 1000

if area < maximum_area:
    print("The area is less than the maximum.")
elif area == maximum_area:
    print("The area is equal to the maximum.")
else:
    print("The area is greater than the maximum.")
