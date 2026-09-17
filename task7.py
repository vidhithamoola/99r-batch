def process_student_results(student_id, student_name, subject_marks, attendance_percentage, assignment_score, extracurricular_points):
    total_marks = 0
    failed_subjects = []

    for subject, marks in subject_marks.items():
        total_marks += marks

        if marks < 35:
            failed_subjects.append(subject)

    average = total_marks / len(subject_marks)
    assignment_contribution = assignment_score * 0.10
    average += assignment_contribution
    average += extracurricular_points

    if attendance_percentage < 75:
        average -= 5
        attendance_status = "Attendance Below 75%"
    else:
        attendance_status = "Good Attendance"

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"

    if len(failed_subjects) > 0:
        result = "Fail"
    else:
        result = "Pass"

    return {
        "student_id": student_id,
        "student_name": student_name,
        "total_marks": total_marks,
        "average": average,
        "grade": grade,
        "attendance_status": attendance_status,
        "failed_subjects": failed_subjects,
        "result": result
    }
student_id = input("Student ID: ")
student_name = input("Student Name: ")

subject_marks = {
    "Math": int(input("Math: ")),
    "Science": int(input("Science: ")),
    "English": int(input("English: ")),
    "Computer": int(input("Computer: ")),
    "Physics": int(input("Physics: "))
}
attendance_percentage = float(input("Attendance Percentage: "))
assignment_score = float(input("Assignment Score: "))
extracurricular_points = float(input("Extracurricular Points: "))

result = process_student_results(
    student_id,
    student_name,
    subject_marks,
    attendance_percentage,
    assignment_score,
    extracurricular_points
)
print()
print("Student ID:", result["student_id"])
print()
print("Student Name:", result["student_name"])
print("Total Marks:", result["total_marks"])
print("Average:", result["average"])
print("Grade:", result["grade"])
print("Attendance Status:", result["attendance_status"])
print("Failed Subjects:", result["failed_subjects"])
print("Result:", result["result"])