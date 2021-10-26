# heights = input("Input a list of student heights: ").split(", ")
# for n in range(0, len(heights)):
#     heights[n] = int(heights[n])
# avg_height = round(sum(heights) / len(heights))
# print(avg_height)
# # solution with sum & len

stud_heights = input("Input a list of student heights: ").split(", ")
for n in range(0, len(stud_heights)):
    stud_heights[n] = int(stud_heights[n])

total_height = 0
for height in stud_heights:
    total_height += height
total_amount = 0
for amount in stud_heights:
    total_amount += 1

avg_height = round(total_height / total_amount)
print(avg_height)
# solution without sum & len, but with for/in
