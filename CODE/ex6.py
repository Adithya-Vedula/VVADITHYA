print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex6.py" + " ============")
# Input the number of quarters, dimes, and nickels from the user
quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))

# Calculate the total monetary value in cents
total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5)

# Print the result
print(f"The coins are worth {total_cents} cents.")
