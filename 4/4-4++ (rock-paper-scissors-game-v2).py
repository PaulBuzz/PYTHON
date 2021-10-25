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

list_of_choices = [rock, paper, scissors]

computer_rock = ["Draw", "User wins", "Computer Wins"]
computer_paper = ["Computer wins", "Draw", "User wins"]
computer_scissors = ["User wins", "Computer wins", "Draw"]
victory_chart = [computer_rock, computer_paper, computer_scissors]

computer_choice = random.randint(0, 2)
user_choice = input(
    "The computer has challenged you to a game of rock, paper, scissors. The computer has made their choice. What is yours? Type 0 for rock, 1 for paper, or 2 for scissors.\n")

print(
    f"Your Choice: \n {list_of_choices[int(user_choice)]}\n The computer's choice: {list_of_choices[int(computer_choice)]} \n {victory_chart[int(computer_choice)][int(user_choice)]}")
