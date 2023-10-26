print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex15.py" + " ============")



#made by adithya

def get_proper_divisors(num):
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def classify_number(num):
    divisors = get_proper_divisors(num)
    divisor_sum = sum(divisors)
    if divisor_sum == num:
        return "Perfect"
    elif divisor_sum < num:
        return "Deficient"
    else:
        return "Abundant"

while True:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        classification = classify_number(num)
        print(f"{num} is a {classification} number.")
    
    choice = input("Do you want to continue (Yes/No)? ").strip().lower()
    if choice != "yes":
        break

#made by adithya
