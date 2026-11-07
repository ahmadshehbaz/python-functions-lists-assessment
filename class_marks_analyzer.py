# This function gets a valid number of students.
def get_student_count():
    while True:
        try:
            count = int(input("How many students are in the class? "))
            if count > 0:
                return count
            else:
                print("Enter at least 1 student.")
        except ValueError:
            print("Please enter a valid whole number.")
# This function gets valid marks between 0 and 100.
def get_valid_mark(name):
    while True:
        try:
            mark = float(input(f"Enter marks for {name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
# This function calculates the class average.
def calculate_average(marks):
    return sum(marks) / len(marks)
# This function displays students with the highest and lowest marks.
def display_extremes(names, marks):
    highest = max(marks)
    lowest = min(marks)
    print("\n===== HIGHEST MARKS =====")
    for i in range(len(marks)):
        if marks[i] == highest:
            print(f"{names[i]}: {marks[i]}")
    print("\n===== LOWEST MARKS =====")
    for i in range(len(marks)):
        if marks[i] == lowest:
            print(f"{names[i]}: {marks[i]}")
# Main program starts here.
print("===== CLASS MARKS ANALYZER =====")
# Create two empty lists.
student_names = []
student_marks = []
# Get the number of students.
total_students = get_student_count()
# Input student names and marks.
for i in range(total_students):
    print(f"\nEnter details of Student {i + 1}")
    name = input("Enter student name: ").strip().title()
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip().title()
    mark = get_valid_mark(name)
    # Store values in their respective lists.
    student_names.append(name)
    student_marks.append(mark)
# Calculate class average.
average = calculate_average(student_marks)
print("\n========== CLASS ANALYSIS ==========")
print(f"Total Students : {len(student_names)}")
print(f"Class Average  : {average:.2f}")
# Display highest and lowest marks.
display_extremes(student_names, student_marks)
# Count passing and failing students.
passing_students = 0
failing_students = 0
for mark in student_marks:
    if mark >= 50:
        passing_students += 1
    else:
        failing_students += 1
print("\n===== PASSING AND FAILING =====")
print(f"Passing Students : {passing_students}")
print(f"Failing Students : {failing_students}")
# Display students scoring above class average.
print("\n===== ABOVE CLASS AVERAGE =====")
found = False
for i in range(len(student_marks)):
    if student_marks[i] > average:
        print(f"{student_names[i]}: {student_marks[i]}")
        found = True
if not found:
    print("No students scored above the class average.")
# Sort students from highest marks to lowest.
print("\n===== RANKING (HIGHEST TO LOWEST) =====")
# Combine names and marks, then sort by marks.
ranked_students = sorted(
    zip(student_names, student_marks),
    key=lambda student: student[1],
    reverse=True
)
for position, (name, mark) in enumerate(ranked_students, start=1):
    print(f"{position}. {name}: {mark}")
print("\n========== ANALYSIS COMPLETE ==========")
