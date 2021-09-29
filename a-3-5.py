print("Welcome to the love calculator!")
name1 = input("Enter your name.\n")
name2 = input("Enter your crush name.\n")

# name1_lower = name1.lower()
# name2_lower = name2.lower()

# t1 = name1_lower.count("t")
# r1 = name1_lower.count("r")
# u1 = name1_lower.count("u")
# e1 = name1_lower.count("e")
# l1 = name1_lower.count("l")
# o1 = name1_lower.count("o")
# v1 = name1_lower.count("v")

# t2 = name2_lower.count("t")
# r2 = name2_lower.count("r")
# u2 = name2_lower.count("u")
# e2 = name2_lower.count("e")
# l2 = name2_lower.count("l")
# o2 = name2_lower.count("o")
# v2 = name2_lower.count("v")

# res1 = t1 + r1 + u1 + e1
# res2 = l1 + o1 + v1 + e1

# res3 = t2 + r2 + u2 + e2
# res4 = l2 + o2 + v2 + e2

# res5 = res1 + res3
# res6 = res2 + res4
# res7 = str(res5) + str(res6)
# print(res7)

# res8 = int(res7)
# if res8 < 10 or res8 > 90:
#     print(f"Your score is {res8} and you match like Coke & Mentos")
# elif res8 <= 40 & res8 >= 50:
#     print(f"Your score is {res8} and you are fine together.")
# else:
#     print(f"Your score is {res8} and you aren't in any of the above lists.")
#
# fully my solution


combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

print(love_score)

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like Coke & Mentos.")
elif (love_score >= 40) & (love_score <= 50):
    print(f"Your score is {love_score}, and you are fine together.")
else:
    print(f"Your score is {love_score}, you don't belong to any group.")

# solution from teacher
