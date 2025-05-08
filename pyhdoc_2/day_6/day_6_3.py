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
