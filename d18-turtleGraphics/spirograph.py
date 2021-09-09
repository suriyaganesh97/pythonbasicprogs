import turtle
from turtle import Turtle
from turtle import Screen
import random
tommy = turtle.Turtle()
turtle.colormode(255)
def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sam_tuple = (r, g, b)
    return sam_tuple


tommy = Turtle()

tommy.speed(0)
gap_bet_circles = 2
for _ in range(int(360/gap_bet_circles)):
    tommy.color(randomcolor())
    tommy.circle(100)
    tommy.setheading(tommy.heading() + gap_bet_circles)






screen = Screen()
screen.exitonclick()