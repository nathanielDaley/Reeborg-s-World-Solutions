def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
