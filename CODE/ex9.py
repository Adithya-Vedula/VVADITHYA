print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex9.py" + " ============")
# Ticket price per ticket
ticket_price = 20

# Input the number of tickets to be bought
num_tickets = int(input("Enter the number of tickets to be bought: "))

# Ensure that the number of tickets is within the allowed range
if num_tickets < 1 or num_tickets > 25:
    print("Tickets cannot be bought. Please enter a valid number between 1 and 25.")
else:
    # Calculate the total cost based on the number of tickets and discounts
    if num_tickets <= 10:
        total_cost = num_tickets * ticket_price
    elif num_tickets <= 20:
        total_cost = num_tickets * ticket_price * 0.9  # 10% discount
    else:
        total_cost = num_tickets * ticket_price * 0.8  # 20% discount

    # Print the total cost
    print(f"The total cost of buying {num_tickets} tickets is: ${total_cost}")
