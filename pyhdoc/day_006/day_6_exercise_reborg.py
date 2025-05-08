## These script should be run on https://reeborg.cs20.ca/


## Exercise - 1: Turn Around
def turn_around():
    turn_left()
    turn_left()


move()
move()
turn_around()
move()
move()
turn_around()

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

## These script should be run on https://reeborg.cs20.ca/

## Exercise 3: Hurdles Loop Challenge


def hurdle1_challenge_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for jump in range(6):
    hurdle1_challenge_step()

## These script should be run on https://reeborg.cs20.ca/

## Exercise 4: While Loop

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle1_challenge_step()
    number_of_hurdles -= 1
