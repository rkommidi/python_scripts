
#Move Robot to desired position, step function returns randam movement

#def step()  -> "UP", "DOWN", "LEFT", "RIGHT

moveRobotTo(1,2)   # Positive integers : RIGHT, UP
moveRobotTo(-2,-3) # Negative integers : LEFT, DOWN

def moveRobotTo(rightSteps, upSteps):
    pos_x = 0
    pos_y = 0
    
    while not (pos_x == rightSteps and pos_y == upSteps):
        result = step()
        if result == "UP":
            pos_y += 1
        elif result == "DOWN":
            pos_y -= 1
        elif result == "LEFT":
            pos_x -= 1
        elif result == "RIGHT":
            pos_x += 1
