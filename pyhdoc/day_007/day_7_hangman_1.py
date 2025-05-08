# Hangman Game Step 1

# randomly choose a word from a list
# if user chooses a wrong letter, wrong is shown
# if user chooses a right letter, right is shown
word_list = ["apple", "grape", "banana", "orange", "lemon"]

import random

random_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for letter in random_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
