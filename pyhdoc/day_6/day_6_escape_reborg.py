## DAY 6 PROJECT Escape the Maze in Reeborg's World
## ----
## These script should be run on https://reeborg.cs20.ca/
## It is tested 3 times.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step_decision():
    # Move until front is clear
    while not front_is_clear():
        turn_left()  # Turn left until a path is clear
    move()

while not at_goal():
    if front_is_clear():
        move()  # Move if no wall ahead
    elif right_is_clear():
        turn_right()  # Turn right if the right is clear
        move()
    else:
        step_decision()  # Handle when there is a wall ahead and on the right
        if front_is_clear():  # Check if the path is clear again after step decision
            move()
