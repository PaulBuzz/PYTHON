import random
print("Let's decide to pays the bill today!")
names_str = input("Enter the names, separated by comma: ")
names = names_str.split(", ")

rand_int = random.randint(0, len(names) - 1)
choiсe = names[rand_int]

print(f"{choiсe} is going to pay for the bill today.")
