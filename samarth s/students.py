students = {
    "Gaurang": {"age": 19, "marks": 80},
    "Rushikesh": {"age": 20, "marks": 95},
    "Krishna": {"age": 21, "marks": 70},
}

print("****** Update the list of students ******")
num_students = int(input("Enter the number of students you want to add: "))

for i in range(num_students):
    name = input("Enter the name of the student: ").strip()
    age = int(input(f"Enter the age of {name}: "))
    marks = int(input(f"Enter the marks of {name} (out of 100): "))
    students[name] = {"age": age, "marks": marks}

print("\n****** Updated List of Students ******")
for name, details in students.items():
    print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")

print("\n****** Calculate Grades ******")
student_name = input("Enter the name of the student to get their grade: ").strip()

if student_name in students:
    marks = students[student_name]["marks"]
    if 91 <= marks <= 100:
        grade = "A"
    elif 81 <= marks <= 90:
        grade = "B"
    elif 71 <= marks <= 80:
        grade = "C"
    elif 35 <= marks <= 70:
        grade = "D"
    else:
        grade = "F"
    print(f"{student_name} has achieved Grade {grade}.")
else:
    print(f"Student {student_name} not found in the list.")
