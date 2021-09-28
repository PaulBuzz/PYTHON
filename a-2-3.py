print('''Let's check how many it's left for you.
What is your age?''')
age = input("Enter your age: ")
age1 = int(age)

days = int((90 - age1) * 365)
weeks = int((90 - age1) * 52)
months = int((90 - age1) * 12)

print(f"You have left {days} days, {weeks} weeks, {months} months to live.")
#  мое самостоятельное решение


# как было решено
# print('''Let's check how many it's left for you.
# What is your age?''')
# age = input("Enter your age: ")

# years = 90 - int(age)

# days = round(years * 365)
# weeks = round(years * 52)
# months = round(years * 12)

# print(f"You have left {days} days, {weeks} weeks, {months} months to live.")
