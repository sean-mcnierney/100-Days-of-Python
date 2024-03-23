def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def follow_right_wall():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()

while not at_goal():
    follow_right_wall()

#This is the solution for the maze portion of reeborg. https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#This took me awhile to get and unfortunately. Progress is never linear I suppose!
