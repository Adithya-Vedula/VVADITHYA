#made by adithya
print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex2.py" + " ============")

import math

# Function to calculate the volume of a cone
def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * (radius**2) * height
    return volume

# Input from the user
radius = float(input("Enter the radius of the cone's base: "))
height = float(input("Enter the height of the cone: "))

# Call the function to calculate and print the volume
cone_volume = calculate_cone_volume(radius, height)
print(f"The volume of the cone is: {cone_volume} cubic units")
