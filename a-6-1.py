import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

chosen_ul = []
for letter in chosen_word:
    chosen_ul += "_"
print(chosen_ul)

guess = input("print the letter: \n").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right.")
    else:
        print("Wrong.")

# if guess in chosen_word:
#     print("yes, there's such letter")
# else:
#     print("Error")

