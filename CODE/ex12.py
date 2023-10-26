print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex12.py" + " ============")
#made by adithya

# Initialize lists to store marks for each test
tests = ["Math", "Science", "English", "IT"]
marks = {test: [] for test in tests}

# Input marks for each student and test
for student in range(1, 11):
    print(f"Enter marks for student {student}:")
    for test in tests:
        mark = int(input(f"{test}: "))
        marks[test].append(mark)

# Calculate highest, lowest, and average marks for each test
for test in tests:
    highest = max(marks[test])
    lowest = min(marks[test])
    average = sum(marks[test]) / len(marks[test])
    print(f"{test} - Highest: {highest}, Lowest: {lowest}, Average: {average:.2f}")

# Calculate highest, lowest, and average marks overall
overall_marks = [mark for sublist in marks.values() for mark in sublist]
highest_overall = max(overall_marks)
lowest_overall = min(overall_marks)
average_overall = sum(overall_marks) / len(overall_marks)
print(f"Overall - Highest: {highest_overall}, Lowest: {lowest_overall}, Average: {average_overall:.2f}")
