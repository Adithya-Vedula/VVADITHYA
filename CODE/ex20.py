print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex20.py" + " ============")


#made by adithya

def calculate_word_potential(word):
    potential = 0
    for char in word:
        if 'A' <= char <= 'Z':
            potential += ord(char) - ord('A') + 65  # Calculate ASCII value and add 65
        elif 'a' <= char <= 'z':
            potential += ord(char) - ord('a') + 65  # Calculate ASCII value and add 65
        else:
            return -1  # Invalid character in the word
    return potential

input_string = input("Enter a string terminated by '.', '?', or '!': ")
word_list = input_string.split()

if input_string[-1] not in ('.', '?', '!'):
    print("INVALID")
else:
    total_potential = 0
    for word in word_list:
        potential = calculate_word_potential(word)
        if potential == -1:
            print("INVALID")
            break
        total_potential += potential
    else:
        print(f"Word potential: {total_potential}")
