print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex18.py" + " ============")

#made by adithya

# Input an email address
email = input("Enter an email address: ")

# Check if the email address contains '@' and '.'
if '@' in email and '.' in email:
    # Split the email address into username and domain
    username, domain = email.split('@')
    # Split the domain into company name and 'com'
    company_name, _ = domain.split('.')
    # Print the company name
    print(company_name)
else:
    print("Invalid email")

#made by adithya
