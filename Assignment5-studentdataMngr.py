# Student Data Manager

students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

# Calculate class average
total = sum(students.values())
average = total / len(students)

# Find topper
topper = max(students, key=students.get)

print("\nStudent Marks:", students)
print("Class Average:", average)
print("Topper:", topper, "with", students[topper], "marks")

# Assign grades
print("\nGrades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(name, ":", grade)