# Complete Snake Game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

def play_game():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        
        # Detect collision with wall
        segment_size = 20
        boundary_x = screen.window_width()//2 - segment_size
        boundary_y = screen.window_height()//2 - segment_size
        if (snake.head.xcor() > boundary_x + segment_size/2 or snake.head.xcor() < -boundary_x - segment_size/2 or snake.head.ycor() > boundary_y + segment_size/2 or snake.head.ycor() < -boundary_y - segment_size/2):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # Ask player if they want to play again            
    answer = screen.textinput("Play Again?", "Do you want to play again? (yes/no)")
    if answer is not None and answer.lower() in ["yes", "y"]:
        play_game() 
    else:
        screen.bye()

play_game()
