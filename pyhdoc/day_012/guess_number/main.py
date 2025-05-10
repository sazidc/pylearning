# Guess The Number Game
import random
import os
from art import logo

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def game():
    clear()
    print(logo)
    print("Welcome to the Guess The Number Game!")
    print("Choose a difficulty. Type 'easy' or 'hard'.")
    difficulty = input().lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty. Please choose 'easy' or 'hard'.")
        return  # Exit the game if the input is invalid

    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess < number:
            print("Too low.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
        print(f"You've run out of attempts. The number was {number}.")

while True:
    game()
    play_again = input("Do you want to play again? Type 'yes' or 'no'. ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")