print("Welcome to the BMI calculator!")
height = input("Enter your height (m): ")
weight = input("Enter your weight (kg): ")
h1 = float(height)
w1 = int(weight)
res = w1 / (h1 ** 2)
res_as_int = int(res)
print(res_as_int)

if res < 18.5:
    print("You are underweight")
elif res >= 18.5 and res < 25:
    print("You are within healthy range")
elif res >= 25 and res < 30:
    print("Your are overweight")
else:
    print("Your are fucking fat, bro")
# BMI calc with if/elif
