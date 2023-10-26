print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex8.py" + " ============")
#made by adithya

# Input the number of whole numbers to sum
num_numbers = int(input("Enter the number of whole numbers to sum: "))

# Initialize variables to store the sums
sum_positive = 0
sum_negative = 0
sum_total = 0

# Read in the numbers and calculate the sums
for _ in range(num_numbers):
    number = int(input("Enter a whole number: "))
    sum_total += number
    if number > 0:
        sum_positive += number
    else:
        sum_negative += number

# Print the sums
print(f"Sum of positive numbers: {sum_positive}")
print(f"Sum of negative numbers: {sum_negative}")
print(f"Sum of all numbers: {sum_total}")

#made by adithya

