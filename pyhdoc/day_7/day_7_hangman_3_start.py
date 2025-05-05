word_list = ['accomplishment', 'authorization', 'cancellation', 'conversation', 'declaration', 'imagination', 'invitation', 'realization', 'recommendation', 'termination']

import random
random_word = random.choice(word_list)
print(f'Psst the solution is {random_word}')

display = []
word_length = len(random_word)  
for letter in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length): 
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
            
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

