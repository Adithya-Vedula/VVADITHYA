print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex21.py" + " ============")




#made by adithy
# Initialize variables to store temperature readings
temperatures = []
highest_temp = 0
lowest_temp = 0
hlist = [] ; llist = []

# Initialize variables to count temperature readings outside the acceptable range
high_temp_count = 0
low_temp_count = 0

# Monitor the baby's temperature every 10 minutes for 2 hours (12 readings)
for i in range(1, 13):
    temp = float(input(f"Enter baby's temperature reading {i} (in °C): "))
    
    # Check if the temperature is within the acceptable range
    if 36.0 <= temp <= 37.5:
        temperatures.append(temp)
        highest_temp = max(highest_temp, temp)
        lowest_temp = min(lowest_temp, temp)
    elif temp > 37.5:
        hlist.append(temp)
        
    elif temp < 36.0:
        llist.append(temp)


# Output the highest and lowest temperatures
print("Max:" , max(hlist))
print("Min:" , min(llist))

# Calculate the temperature difference
temp_difference = max(hlist) - min(llist)
print(f"Temperature difference: {temp_difference:.1f}°C")

# Check if the baby's condition is concerning
if temp_difference > 1.0 or high_temp_count > 2 or low_temp_count > 2:
    print("Baby's condition may be concerning. Please consult a doctor.")

