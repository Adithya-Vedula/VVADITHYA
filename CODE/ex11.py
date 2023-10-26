print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex11.py" + " ============")
# Input the number of calls
#made by adithya
num_calls = int(input("Enter the number of calls: "))

# Initial cost for the first 100 calls
total_cost = 200

# Calculate additional charges for calls over 100
if num_calls > 100:
    num_calls_over_100 = num_calls - 100
    total_cost += min(num_calls_over_100, 50) * 0.60
    num_calls_over_100 -= min(num_calls_over_100, 50)
    total_cost += num_calls_over_100 * 0.50

# Add extra charge if calls exceed 200
if num_calls > 200:
    total_cost += (num_calls - 200) * 0.40

# Print the total cost
print(f"The monthly phone cost is: Rs {total_cost}")

