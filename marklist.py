def calculate_average_mark(marks):
    total_marks = sum(marks)
    num_of_subjects = len(marks)
    average_mark = total_marks / num_of_subjects
    return average_mark
num_of_subjects = int(input("Enter the number of subjects:"))
marks = []
for i in range(num_of_subjects):
    mark = float(input(f"Enter the mark for subject {i+1}: "))
    marks.append(mark)
average = calculate_average_mark(marks)
print("Average mark:", average)