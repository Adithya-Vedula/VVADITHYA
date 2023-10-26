#made by adithya - ex1
print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex1.py" + " ============")
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Input from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Call the function to convert and print the result
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
