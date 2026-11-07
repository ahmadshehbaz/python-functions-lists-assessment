# This function cleans the student's name.
def format_name(name):
    return name.strip().title()
# This function gets valid marks between 0 and 100.
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
# This function calculates the percentage.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100
# This function determines the letter grade.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"
# Main program starts here.
print("===== STUDENT RESULT CARD GENERATOR =====")
# Get student information.
name = format_name(input("Enter student name: "))
while True:
    roll_number = input("Enter roll number: ").strip()
    if roll_number.isdigit():
        break
    else:
        print("Invalid roll number! Digits only.")
# Get marks in five subjects.
subjects = ["English", "Math", "Computer", "Physics", "Chemistry"]
student_marks = []
for subject in subjects:
    marks = get_valid_marks(subject)
    student_marks.append(marks)
# Calculate total and percentage.
total = sum(student_marks)
max_total = 500
percentage = calculate_percentage(total, max_total)
# Calculate grade.
grade = get_grade(percentage)
# Check whether any subject marks are below 40.
if any(mark < 40 for mark in student_marks):
    status = "Fail"
else:
    status = "Pass"
# Display result card.
print("\n" + "=" * 40)
print("           STUDENT RESULT CARD")
print("=" * 40)
print(f"Student Name  : {name}")
print(f"Roll Number   : {roll_number}")
print("-" * 40)
print("SUBJECT             MARKS")
print("-" * 40)
for subject, mark in zip(subjects, student_marks):
    print(f"{subject:<20} {mark:>6.2f}")
print("-" * 40)
print(f"Total Marks   : {total} / {max_total}")
print(f"Percentage    : {percentage:.2f}%")
print(f"Grade         : {grade}")
print(f"Final Status  : {status}")
print("=" * 40)
