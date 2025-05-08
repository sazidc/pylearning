## These script should be run on https://reeborg.cs20.ca/

## Exercise - 2: Four Square

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def four_square_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_around()

four_square_move()
