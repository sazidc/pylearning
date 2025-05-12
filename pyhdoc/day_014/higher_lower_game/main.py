# Higher Lower Game

from art import logo, vs
from game_data import data
import random
import os

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def get_celebrity(celebrity):
    """Returns formatted celebrity data."""
    return f"{celebrity['name']}, a {celebrity['description']}, from {celebrity['country']}"

def compare_follower_count(follower_count1, follower_count2):
    """Returns the higher follower count."""
    if follower_count1 > follower_count2:
        return "a"
    else:
        return "b"

def play_game():
    """Play a game of Higher Lower."""
    
    print(logo)
    
    score = 0
    game_should_continue = True
    
    # Select the first celebrity
    celebrity_A = random.choice(data)
    
    while game_should_continue:
        # Select a different celebrity for B
        celebrity_B = random.choice(data)
        while celebrity_B == celebrity_A:  # Ensure A and B are different
            celebrity_B = random.choice(data)
        
        # Get follower counts
        celebrity_A_follower_count = celebrity_A["follower_count"]
        celebrity_B_follower_count = celebrity_B["follower_count"]
        
        print(f"Compare A: {get_celebrity(celebrity_A)}")
        print(f"Follower Count: {celebrity_A_follower_count}")
        print(vs)
        print(f"Against B: {get_celebrity(celebrity_B)}")
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        clear()
        print(logo)
        
        correct_answer = compare_follower_count(celebrity_A_follower_count, celebrity_B_follower_count)
        
        if correct_answer == user_guess:
            score += 1
            print(f"You're right! Current score: {score}")
            # update celebrity_A with the winner
            if correct_answer == "a":
                celebrity_A = celebrity_A # keep celebrity_A
            else:
                celebrity_A = celebrity_B # celebrity_B is now celebrity_A
        # move on to the next round
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
play_game()

# Ask if the user wants to play again
while input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()

print("Thanks for playing!")
