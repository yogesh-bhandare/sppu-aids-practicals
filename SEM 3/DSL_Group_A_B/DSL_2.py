def calculate_average(marks):
    total = 0
    count = 0
    for mark in marks:
        total += mark
        count += 1
    if count == 0:
        return 0  # Avoid division by zero if there are no valid marks
    return total / count


def find_highest_and_lowest(marks):
    if not marks:
        return None, None  # Return None for both highest and lowest if there are no valid marks

    highest = lowest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    return highest, lowest


def count_absent_students(marks, absent_mark):
    count = 0
    for mark in marks:
        if mark == absent_mark:
            count += 1
    return count


def find_most_frequent_mark(marks):
    if not marks:
        return None  # Return None if there are no valid marks

    frequency = {}
    most_frequent_marks = []
    max_frequency = 0

    for mark in marks:
        if mark in frequency:
            frequency[mark] += 1
        else:
            frequency[mark] = 1

        if frequency[mark] > max_frequency:
            max_frequency = frequency[mark]
            most_frequent_marks = [mark]
        elif frequency[mark] == max_frequency and mark not in most_frequent_marks:
            most_frequent_marks.append(mark)

    return most_frequent_marks


# Input the number of students
num_students = int(input("Enter the total number of students: "))

# Initialize an empty list to store marks
marks = []

# Input marks for each student
i = 0
while i < num_students:
    mark = input(f"Enter the mark for student {i + 1} (or 'ab' for absent): ")

    if mark.lower() == 'ab':
        # Handle absent students by assigning a special value (e.g., -1)
        marks.append(-1)
    else:
        marks.append(int(mark))

    i += 1

# Calculate the average
average = calculate_average([mark for mark in marks if mark != -1])

# Find the highest and lowest marks
highest, lowest = find_highest_and_lowest([mark for mark in marks if mark != -1])

# Count absent students
absent_count = count_absent_students(marks, -1)

# Find the most frequent mark(s)
most_frequent_marks = find_most_frequent_mark([mark for mark in marks if mark != -1])

# Display the results
print(f"Average score of the class: {average}")
print(f"Highest score of the class: {highest}")
print(f"Lowest score of the class: {lowest}")
print(f"Count of absent students: {absent_count}")
if most_frequent_marks:
    print(f"Mark(s) with the highest frequency: {', '.join(map(str, most_frequent_marks))}")
else:
    print("There are no valid marks to determine the most frequent mark.")
