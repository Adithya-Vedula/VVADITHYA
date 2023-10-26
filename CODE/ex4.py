#made by adithya
print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex4.py" + " ============")

amount = int(input("Enter the amount in Rial (OMR): "))
denominations = [50, 20, 10, 5, 1]

for denomination in denominations:
    notes = amount // denomination
    amount %= denomination
    print(f"RO {denomination} - {notes}")
