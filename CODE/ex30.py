print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex30.py" + " ============")


#made by adithya
import random

def generate_random_numbers(N):
    random_numbers = []
    for x in range(N):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)
    return random_numbers

def find_highest_and_lowest(numbers):
    if not numbers:
        return None, None
    highest = max(numbers)
    lowest = min(numbers)
    return highest, lowest

# Input: Number of random numbers to generate
N = int(input("Enter the number of random numbers to generate: "))

random_numbers = generate_random_numbers(N)
highest, lowest = find_highest_and_lowest(random_numbers)

print(f"Generated random numbers: {random_numbers}")
print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
