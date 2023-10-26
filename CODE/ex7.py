print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex7.py" + " ============")
#made by adithya

# Input the maximum room capacity and the number of people attending the meeting
max_capacity = int(input("Enter the maximum room capacity: "))
num_attendees = int(input("Enter the number of people attending the meeting: "))

# Check if the number of people is within the legal limit
if num_attendees <= max_capacity:
    print("It is legal to hold the meeting.")
else:
    excess_people = num_attendees - max_capacity
    print(f"The meeting cannot be held. {excess_people} people must leave.")
