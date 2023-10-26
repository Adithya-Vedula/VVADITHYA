print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex17.py" + " ============")

#made by adithya

# Input an email address
email = input("Enter an email address: ")

# Check if the email address contains '@' and '.'
if '@' in email and '.' in email:
    # Split the email address into username and domain
    username, domain = email.split('@')
    # Print the username with the first letter capitalized
    print(username.capitalize())
else:
    print("Invalid email")

#made by adithya

