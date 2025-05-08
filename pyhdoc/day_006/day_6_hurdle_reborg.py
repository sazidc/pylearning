## These script should be run on https://reeborg.cs20.ca/

## Hurdle 2

while at_goal() != True:  ## while not at_goal():
    hurdle1_challenge_step()

## Hurdle 3


def hurdle_step():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        hurdle_step()
    else:
        move()

## Hurdle 4


def modified_hurdle_step():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if wall_in_front():
        modified_hurdle_step()
    else:
        move()
