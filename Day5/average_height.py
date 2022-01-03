student_heights = input("Enter student heights: ").split(",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# By using functions
# total_height = sum(student_heights)
# num_students = len(student_heights)
# average_height = total_height / num_students

# By using a for loop

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

num_students = 0
for student in student_heights:
    num_students += 1
print(num_students)

average_height = total_height / num_students
print(average_height)