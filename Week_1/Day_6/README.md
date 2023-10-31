This day we learned about Python Functions and While Loops. We also used Reeborg's World to train defining function and using loops, it's a little website reeborg.ca where there's a robot and you have to make him do something, like finding is way trought a maze, jumping obstacles with programming, was a really nice way to program something and see the effects in the robot.

This was the final part of Reedborg exercise: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json  My code should already load with the page, but in case not:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def walk():
    move()
    jump()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


Actually today the final project is also on Reeborg's World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json The objective is to always escape the Maze, the initial position AND orientation is random.

My code for this day was way simply than i expected... I've read somewhere i long time ago, if you ever get stuck in a Maze, you should stick to the right wall and follow it's path, i tried to replicate that idea on my code, and well, it worked...

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    elif wall_on_right:
        turn_left()

Now this day i'll not have a .py file since it's on a website, but i posted the link in here in case anyone wants to test it out!

After seeing the solution from the teacher, i figured out that she also create 3 maps for to test our code at, because there's some situations that maybe our code could have create a eternal loop, i didn't had this problem with the normal map, i tried several times always worked, but now with the custom maps from the teacher, it create a eternal loop in 2 out of 3... Gonna remake the code

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

Ok, now this code work out for every scenario available to us!!!