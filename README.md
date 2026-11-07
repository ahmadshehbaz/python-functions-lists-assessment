# Python Student Management & Marks Analysis

## 1. Project Overview

This project contains two separate Python programs developed to practice basic Python programming concepts.

The main purpose of this project is to understand how Python functions, lists, loops, conditional statements, string manipulation, and input validation work in real-world programs.

Both programs take input from users, process the information, and display organized results.

## 2. Programs Description

### Task 1: Student Result Card Generator

This program generates a result card for an individual student.

**Features:**
- Takes the student's name and roll number.
- Accepts marks in five different subjects.
- Validates marks to ensure they are between 0 and 100.
- Validates the roll number using the `isdigit()` method.
- Cleans the student's name using `strip()` and `title()`.
- Calculates total obtained marks and overall percentage.
- Assigns a grade according to the percentage.
- Declares the final result as Pass or Fail.
- Automatically declares the student Fail if any subject mark is below 40.
- Displays a properly formatted result card using f-strings.

**Grading Criteria:**

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | Fail |

### Task 2: Class Marks Analyzer

This program analyzes the academic performance of an entire class.

**Features:**
- Asks the user how many students are in the class.
- Takes each student's name and marks.
- Stores names and marks in two separate lists.
- Validates marks between 0 and 100.
- Calculates the class average.
- Finds the highest and lowest marks.
- Displays the names of students who achieved the highest and lowest marks.
- Counts passing students (50 or above).
- Counts failing students (below 50).
- Displays students who scored above the class average.
- Sorts students' marks from highest to lowest.

## 3. Python Concepts and Functions Used

The following Python concepts and built-in functions are used in this project.

| Concept / Function | Description |
|---|---|
| `def` | Defines custom functions. |
| Parameters | Pass information into functions. |
| `return` | Returns a result from a function. |
| `input()` | Takes input from the user. |
| `print()` | Displays output. |
| `if`, `elif`, `else` | Apply conditional logic. |
| `while` loop | Repeats input until valid data is entered. |
| `for` loop | Iterates through subjects and students. |
| `try` and `except` | Handle invalid input errors. |
| `float()` | Converts input into decimal numbers. |
| `int()` | Converts input into integers. |
| `.isdigit()` | Checks whether a string contains only digits. |
| `.strip()` | Removes unnecessary spaces. |
| `.title()` | Capitalizes the first letter of each word. |
| `.append()` | Adds items to a list. |
| `len()` | Returns the number of items. |
| `sum()` | Calculates the sum of marks. |
| `max()` | Finds the highest marks. |
| `min()` | Finds the lowest marks. |
| `sorted()` | Sorts student records. |
| `zip()` | Combines student names and marks. |
| `enumerate()` | Provides a position number while looping. |
| `f-strings` | Formats output strings. |
| `any()` | Checks whether at least one subject has marks below 40. |
| `lambda` | Creates a small anonymous function for sorting. |

### Custom Functions

**Task 1:**
- `format_name(name)`
- `get_valid_marks(subject)`
- `calculate_percentage(total, max_total)`
- `get_grade(percentage)`

**Task 2:**
- `get_student_count()`
- `get_valid_mark(name)`
- `calculate_average(marks)`
- `display_extremes(names, marks)`

## 4. Project Structure

The project contains the following files:

```text
Student-Management-Project/
│
├── task1_result_card.py
├── task2_marks_analyzer.py
└── README.md
```

- `task1_result_card.py`: Generates an individual student's result card.
- `task2_marks_analyzer.py`: Analyzes the marks of an entire class.
- `README.md`: Contains project documentation and instructions.

## 5. Requirements

To run this project, you need:

- Python 3.x installed on your computer.
- A code editor such as Visual Studio Code or PyCharm.
- A terminal or command prompt.

No external Python libraries are required.

## 6. How to Run the Programs

### Step 1: Download or Clone the Project

Download the project files and open the project folder in your code editor.

### Step 2: Open the Terminal

Open the terminal inside your project folder.

### Step 3: Run Task 1

Execute the following command:

```bash
python task1_result_card.py
```

### Step 4: Run Task 2

Execute the following command:

```bash
python task2_marks_analyzer.py
```

**Note:** On some systems, you may need to use `python3` instead of `python`.

## 7. Sample Input and Output

### Task 1: Student Result Card Generator

**Sample Input:**

```text
Enter student name: ahmad ali
Enter roll number: 12345
Enter marks for English: 90
Enter marks for Math: 85
Enter marks for Computer: 95
Enter marks for Physics: 80
Enter marks for Chemistry: 90
```

**Sample Output:**

```text
========================================
           STUDENT RESULT CARD
========================================
Student Name  : Ahmad Ali
Roll Number   : 12345
----------------------------------------
SUBJECT             MARKS
----------------------------------------
English               90.00
Math                  85.00
Computer              95.00
Physics               80.00
Chemistry             90.00
----------------------------------------
Total Marks   : 440.0 / 500
Percentage    : 88.00%
Grade         : A
Final Status  : Pass
========================================
```

### Task 2: Class Marks Analyzer

**Sample Input:**

```text
How many students are in the class? 5

Enter details of Student 1
Enter student name: Ahmad
Enter marks for Ahmad: 85

Enter details of Student 2
Enter student name: Ali
Enter marks for Ali: 95

Enter details of Student 3
Enter student name: Sara
Enter marks for Sara: 65

Enter details of Student 4
Enter student name: Hamza
Enter marks for Hamza: 45

Enter details of Student 5
Enter student name: Usman
Enter marks for Usman: 95
```

**Sample Output:**

```text
========== CLASS ANALYSIS ==========
Total Students : 5
Class Average  : 77.00

===== HIGHEST MARKS =====
Ali: 95.0
Usman: 95.0

===== LOWEST MARKS =====
Hamza: 45.0

===== PASSING AND FAILING =====
Passing Students : 4
Failing Students : 1

===== ABOVE CLASS AVERAGE =====
Ahmad: 85.0
Ali: 95.0
Usman: 95.0

===== RANKING (HIGHEST TO LOWEST) =====
1. Ali: 95.0
2. Usman: 95.0
3. Ahmad: 85.0
4. Sara: 65.0
5. Hamza: 45.0

========== ANALYSIS COMPLETE ==========
```

## 8. Input Validation and Error Handling

Both programs include input validation to prevent incorrect data.

Examples:

- Marks below 0 or above 100 are rejected.
- Non-numeric marks are rejected.
- Invalid roll numbers are rejected.
- Empty student names are not accepted in Task 2.
- Invalid student counts are rejected.
- The programs ask the user to enter valid information again.

## 9. Conclusion

This project helped develop a better understanding of Python fundamentals through practical programming.

By completing these two tasks, I practiced:

- Creating and calling custom functions.
- Working with parameters and return values.
- Using lists to store and manage data.
- Applying loops and conditional statements.
- Validating user input and handling errors.
- Manipulating strings.
- Calculating percentages and averages.
- Sorting and analyzing student records.

These programs demonstrate how basic Python concepts can be combined to solve practical problems.