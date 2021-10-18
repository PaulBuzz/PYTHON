print("Let's order some pizza!")
size = input("Please choose the size. S(15$), M(20$), L(25$) ")
add_pepper = input("Would you like some pepperoni? S(2$), M/L(3$) Y / N ")
extra_cheese = input("Would you like some extra cheese? S/M/L(1$) Y / N ")
bill = 0

if size == "S":
    bill = 15
    if add_pepper == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill = {bill}$.")
if size == "M":
    bill = 20
    if add_pepper == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill = {bill}$.")
if size == "L":
    bill = 25
    if add_pepper == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill = {bill}$.")
# моё собственное решение

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepper == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is {bill}$.")
# решение в курсе
