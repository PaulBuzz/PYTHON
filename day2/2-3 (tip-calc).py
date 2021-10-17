print("Welcome to the tip calculator!")
bill = float(input("Total bill is $ "))
tip = int(input("What is the percentage of tip? Choose from 10, 12, 15. "))
people = int(input("How many people will share the bill? "))

# tip_as_perc = tip / 100
# total_tip = bill * tip_as_perc
# total_bill = bill + total_tip
# each = total_bill / people
# print(f"Each person should pay: $ {each:.2f}")

bill_per_person = bill / people
bill_with_tip = (bill_per_person / 100) * tip
total = bill_per_person + bill_with_tip
print(f"Each person should pay: $ {total:.2f}")

# :.2f = 2 знака после точки в f-String
