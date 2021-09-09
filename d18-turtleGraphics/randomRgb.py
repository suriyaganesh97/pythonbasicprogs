import turtle
from turtle import Screen
import random

turtle.colormode(255)
def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sam_tuple = (r, g, b)
    return sam_tuple


tommy = turtle.Turtle()
tommy.width(7)
tommy.speed(0)
angle_choice = [90, 180, 360]
steps_choice = [10, 20, 30]

for _ in range(0, 200):
    tommy.color(randomcolor())
    tommy.forward(random.choice(steps_choice))
    tommy.right(random.choice(angle_choice))


screen = Screen()
screen.exitonclick()