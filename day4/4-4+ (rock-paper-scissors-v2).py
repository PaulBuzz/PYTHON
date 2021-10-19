import random
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

images = [rock, paper, scissors]


user_choice = int(input(
    "Let's play rock/paper/scissors game. Choose 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number and you therefore lose.")
else:
    print(f"You chose: {images[user_choice]}")

    comp_choice = random.randint(0, 2)
    print(f"Computer chose: {images[comp_choice]}")

    if user_choice == 0 & comp_choice == 2:
        print("You win.")
    elif comp_choice == 0 & user_choice == 2:
        print("You lose.")
    elif comp_choice > user_choice:
        print("You lose.")
    elif user_choice > comp_choice:
        print("You win.")
    elif comp_choice == user_choice:
        print("It's a draw.")
