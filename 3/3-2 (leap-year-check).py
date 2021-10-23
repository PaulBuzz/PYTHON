print("Let's check if the year if leap.")
year = int(input("Please enter the year here: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year.")
        else:
            print("It's not a leap year.")
    else:
        print("It's a leap year.")
else:
    print("It's not a leap year.")
