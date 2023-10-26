print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex22.py" + " ============")

#made by adithya

# Input a list with an even number of elements
L = [10, 20, 30, 40, 50, 60]

# Check if the list has an even number of elements
if len(L) % 2 == 0:
    # Exchange the first and second halves of the list
    L = L[len(L) // 2:] + L[:len(L) // 2]

    # Calculate the sums of the first and second halves
    first_half_sum = sum(L[:len(L) // 2])
    second_half_sum = sum(L[len(L) // 2:])

    # Output the results
    print("List after exchange:", L)
    print("Sum of elements in the first half:", first_half_sum)
    print("Sum of elements in the second half:", second_half_sum)
else:
    print("The list must have an even number of elements for this operation.")

#made by adithya

