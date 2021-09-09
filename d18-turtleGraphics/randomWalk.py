from turtle import Turtle
from turtle import Screen
import random

tommy = Turtle()

tommy.shape("turtle")
tommy.width(7)
tommy.speed(0)
colour_choices = ["red", "blue", "green", "black", "brown"]

steps_choice = [10, 20, 30]
angle_choice = [90, 180, 360]
for _ in range(300):
    tommy.color(random.choice(colour_choices))
    tommy.forward(random.choice(steps_choice))
    tommy.right(random.choice(angle_choice))



screen = Screen()
screen.exitonclick()