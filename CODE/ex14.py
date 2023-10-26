print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex14.py" + " ============")
#made by adithya

# Initialize lists to store the entered numbers
numbers = []

# Initialize counters for numbers entered and the maximum/minimum numbers
count = 0
max_num = None
min_num = None

# Loop to input numbers
while count < 5:
    try:
        num = float(input("Enter a number greater than zero: "))
        if num > 0:
            numbers.append(num)
            count += 1
            if max_num is None or num > max_num:
                max_num = num
            if min_num is None or num < min_num:
                min_num = num
        else:
            print("Please enter a number greater than zero.")

        choice = input("Do you want to continue (Yes/No)? ").strip().lower()
        if choice != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if at least 5 numbers were entered
if count >= 5:
    print("Maximum number entered:", max_num)
    print("Minimum number entered:", min_num)
else:
    print("You did not enter at least 5 valid numbers.")
