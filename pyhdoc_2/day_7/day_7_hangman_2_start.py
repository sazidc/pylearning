# adding to the previous file so the words letters will be replaced with underscores

word_list = ['accomplishment', 'authorization', 'cancellation', 'conversation', 'declaration', 'imagination', 'invitation', 'realization', 'recommendation', 'termination']

import random
random_word = random.choice(word_list)
print(f'Psst the solution is {random_word}')

display = []
word_length = len(random_word)  
for letter in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length): 
    letter = random_word[position]
    if letter == guess:
        display[position] = letter
        
# loop through each letter in the random_word and replace the corresponding underscore for right letter
# print display after the guess
print(display)

