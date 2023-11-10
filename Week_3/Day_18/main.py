"""
from turtle import Turtle, Screen
import random

tsu_the_turtle = Turtle()
tsu_the_turtle.shape("turtle")

tsu_speed = ["fastest", "fast", "normal", "slow", "slowest"]
directions = [0, 90, 180, 270]
tsu_the_turtle.pensize(5)

def random_walk(number_walks):
    while number_walks > 0:
        tsu_the_turtle.color(random.random(), random.random(), random.random())
        tsu_the_turtle.forward(10)
        tsu_the_turtle.setheading(random.choice(directions))
        tsu_the_turtle.speed(tsu_speed[0])
        number_walks -= 1


random_walk(random.randint(0,250))
"""

import turtle as turtle_module
import random

turtle_module.colormode(255)
tsu = turtle_module.Turtle()
tsu.speed("fastest")
tsu.penup()
tsu.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tsu.setheading(225)
tsu.forward(300)
tsu.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tsu.dot(20, random.choice(color_list))
    tsu.forward(50)

    if dot_count % 10 == 0:
        tsu.setheading(90)
        tsu.forward(50)
        tsu.setheading(180)
        tsu.forward(500)
        tsu.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()











screen = Screen()
screen.exitonclick()