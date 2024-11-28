student_scores = {}

student_grades = {}

print("Welcome to the Scores to Grades Converter.")
number_of_students  = int(input("Enter the total number of students, whose scores you want to convert: "))
for i in range(number_of_students) :
    name = input("What is the name of the student: ")
    student_scores[name] = int(input("What is his score : "))

for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "A"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "B"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "C"
    elif 61 <= student_scores[key] <= 70:
        student_grades[key] = "D"
    elif 51 <= student_scores[key] <= 60:
        student_grades[key] = "P"
    else:
        student_grades[key] = "Fail"
print("\n" * 100)
print("The grades of the students are:")
for key in student_grades :
    print(f"{key} = {student_grades[key]}")
