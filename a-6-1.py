import random
from logo import logo, stages
import words

print(logo)

chosen_word = random.choice(words.word_list)
print(f"The word to guess has {len(chosen_word)} letters.")

chosen_ul = []
word_length = len(chosen_word)
for _ in range(word_length):
    chosen_ul += "_"
print(chosen_ul)

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("print the letter: \n").lower()

    if guess in chosen_ul:
        print(f"You've already guessed the letter {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            chosen_ul[position] = letter
    print(chosen_ul)

    if guess not in chosen_word:
        print(f"You've guessed {guess} and it's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in chosen_ul:
        end_of_game = True
        print("You win.")
    print(stages[lives])