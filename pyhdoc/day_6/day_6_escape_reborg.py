## DAY 6 PROJECT Escape the Maze in Reeborg's World
## ----
## 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step_decision():
    if not front_is_clear():
        while not front_is_clear():
            turn_left()
        move()