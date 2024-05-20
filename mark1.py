def calculate_average_mark(marks):
    total_marks = sum(marks)
    num_of_subjects = len(marks)
    average_mark = total_marks / num_of_subjects
    return average_mark

num_of_students = int(input("Enter the number of students: "))
num_of_subjects = int(input("Enter the number of subjects: "))

student_marks = {}

for i in range(num_of_students):
    student_name = input(f"Enter the name of student {i+1}: ")
    marks = []
    for j in range(num_of_subjects):
        mark = float(input(f"Enter the mark for subject {j+1}: "))
        marks.append(mark)
    student_marks[student_name] = marks

print("\nAverage marks for each student:")
for student, marks in student_marks.items():
    average_mark = calculate_average_mark(marks)
    print(f"{student}: {average_mark}")