stud_score = input("Enter the list of scores: ").split(", ")
for n in range(0, len(stud_score)):
    stud_score[n] = int(stud_score[n])
max_score = 0
for score in stud_score:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")
# high score using for/in loop and without max() func
