print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex10.py" + " ============")
#made by adithya

# Destination and corresponding charges per adult
destination_charges = {
    "Ambala": 500,
    "Chandigarh": 800,
    "Anandpur Sahib": 900
}

# Input the destination and the number of adults and kids
destination = input("Enter the destination (Ambala, Chandigarh, or Anandpur Sahib): ")
num_adults = int(input("Enter the number of adults: "))
num_kids = int(input("Enter the number of kids (below 12 years old): "))

# Calculate the total charge for adults and kids
adult_charge = destination_charges.get(destination, 0)
kids_charge = 0.2 * adult_charge  # 20% of adult charge

total_charge = (num_adults * adult_charge) + (num_kids * kids_charge)
discount = 0
# Apply a 15% discount if the total charge exceeds Rs 10,000
if total_charge > 10000:
    discount = 0.15 * total_charge
    total_charge -= discount

# Calculate the net payable amount
net_payable_amount = total_charge - discount

# Print the total charge, discount, and net payable amount
print(f"Total charge: Rs {total_charge}")
if discount > 0:
    print(f"15% Discount Applied: Rs {discount}")
print(f"Net Payable Amount: Rs {net_payable_amount}")

#made by adithya

