import random
game = input(
    "Let's play rock/paper/scissors game. Choose 0 for Rock, 1 for Paper, 2 for Scissors: \n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_choice = random.randint(0, 2)

a = game == "0"
b = game == "1"
c = game == "2"
a1 = random_choice == 0
b1 = random_choice == 1
c1 = random_choice == 2

if a == True:
    print(f"You chose: ", rock)
elif b == True:
    print(f"You chose: ", paper)
elif c == True:
    print(f"You chose: ", scissors)
else:
    print("There's no such figure.")

if a1 == True:
    print(f"Computer chose: ", rock)
elif b1 == True:
    print(f"Computer chose: ", paper)
elif c1 == True:
    print(f"Computer chose: ", scissors)

if a & a1 == True:
    print("It's a draw.")
elif b & b1 == True:
    print("It's a draw.")
elif c & c1 == True:
    print("It's a draw.")

if a == True & b1 == True:
    print("Computer wins.")
elif a == True & c1 == True:
    print("You win.")
elif b == True & a1 == True:
    print("You win.")
elif b == True & c1 == True:
    print("Computer wins.")
elif c == True & b1 == True:
    print("You win.")
elif c == True & a1 == True:
    print("Computer wins.")
# fully my solution
