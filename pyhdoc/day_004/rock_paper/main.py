import random

# Rock, Paper, Scissors ASCII Art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

# Initialize scores
user_score = 0
computer_score = 0
rounds = 0

while rounds < 3:
    # Prompt user for their choice
    try:
        user_choice = int(
            input(
                "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
            )
        )
        # Check if the input is valid (0, 1, or 2)
        if user_choice < 0 or user_choice > 2:
            print("Invalid choice! Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        continue

    # Show the user's choice
    print(game_images[user_choice])

    # Computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine winner of the round
    if user_choice == 0 and computer_choice == 2:
        print("You win this round!")
        user_score += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose this round!")
        computer_score += 1
    elif computer_choice > user_choice:
        print("You lose this round!")
        computer_score += 1
    elif user_choice > computer_choice:
        print("You win this round!")
        user_score += 1
    elif computer_choice == user_choice:
        print("It's a draw for this round!")

    rounds += 1

# After 3 rounds, determine the overall winner
print(f"\nFinal Scores: You: {user_score} - Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You win the best of 3!")
elif computer_score > user_score:
    print("Sorry, you lose the best of 3.")
else:
    print("It's a draw for the best of 3.")

print("Thanks for playing!")
