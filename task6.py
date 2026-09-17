def display_student(student_id, name):
    print("Student Details")
    print("Student ID:", student_id)
    print("Student Name:", name)
def calculate_total(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    print("Total Marks:", total)
def calculate_percentage(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5
    print("Percentage:", percentage, "%")
def find_grade(percentage):
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 40:
        print("Grade: D")
    else:
        print("Grade: Fail")
def highest_mark(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    print("Highest Mark:", highest)
def lowest_mark(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    print("Lowest Mark:", lowest)
def pass_fail(mark1, mark2, mark3, mark4, mark5):
    if mark1 < 35 or mark2 < 35 or mark3 < 35 or mark4 < 35 or mark5 < 35:
        print("Result: Fail")
    else:
        print("Result: Pass")
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))
mark4 = int(input("Enter Subject 4 Marks: "))
mark5 = int(input("Enter Subject 5 Marks: "))
percentage = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
display_student(student_id, name)
print()
calculate_total(mark1, mark2, mark3, mark4, mark5)
print()
calculate_percentage(mark1, mark2, mark3, mark4, mark5)
print()
find_grade(percentage)
print()
highest_mark(mark1, mark2, mark3, mark4, mark5)
print()
lowest_mark(mark1, mark2, mark3, mark4, mark5)
print()
pass_fail(mark1, mark2, mark3, mark4, mark5)