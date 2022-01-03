student_scores = input("Enter the scores of the students: ").split(",")

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Find the highest score using  in-built function
# highest_score = max(student_scores)

# Find the highest score using loops
highest_score = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]
print("The highest score is: ", highest_score)
