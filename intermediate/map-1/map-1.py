#Traditional way
move()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
move()
turn_left()

move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
move()


turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
move()
turn_left()

move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
move()
turn_left()


move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
move()
turn_left()

move()
turn_left()
turn_left()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

#Using functions


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
jump()
jump()
jump()
jump()
jump()
jump()



#Using function and for loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    jump()

#using IF statement and for loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(6):   
    if front_is_clear():
        move()
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()