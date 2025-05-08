import random
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo at the start of the game
print(logo)

# Create blanks to represent the word
display = ["_"] * word_length

# List to track the guessed letters
guessed_letters = []

while not end_of_game:
    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if the input is a valid single letter
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter.")
        continue

    # Check if the user has already guessed this letter
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    # Add the guessed letter to the guessed letters list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Update the display list with the correctly guessed letter
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            # Print the number of lives left
        print(f"You have {lives} lives left.")


    # Print the current progress of the word
    print(" ".join(display))

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the hangman stage based on the number of lives left
    print(stages[lives])
