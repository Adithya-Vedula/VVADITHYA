print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex13.py" + " ============")
#made by adithya

# Function to print Armstrong numbers up to a given limit N


# Input the limit from the user
N = int(input("Enter the end limit (N): "))
for num in range(N):
    s = 0
    for i in str(num):
        s += int(i)**3
    if s == num:
        print("ARMSTRONG NUMBER",num)

#made by adithya
