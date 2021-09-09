from turtle import Turtle
from turtle import Screen
import random

tommy = Turtle()
tommy.shape("turtle")
# #triangle
# tommy.color("red")
# for _ in range(3):
#     tommy.forward(100)
#     tommy.right(120)
#
# #square
# tommy.color("blue")
# for _ in range(4):
#     tommy.forward(100)
#     tommy.right(90)
#
# #pentagon
# tommy.color("black")
# for _ in range(5):
#     tommy.forward(100)
#     tommy.right(72)
#
# #hexagon
# tommy.color("red")
# for _ in range(6):
#     tommy.forward(100)
#     tommy.right(60)
#
# #heptogon
# tommy.color("blue")
# for _ in range(7):
#     tommy.forward(100)
#     tommy.right(51.43)
#
# #ocatgon
# tommy.color("black")
# for _ in range(8):
#     tommy.forward(100)
#     tommy.right(45)
#
# #nonagon
# tommy.color("red")
# for _ in range(9):
#     tommy.forward(100)
#     tommy.right(40)
#
# #ocatgon
# tommy.color("blue")
# for _ in range(10):
#     tommy.forward(100)
#     tommy.right(36)

no_of_sides = 3
while no_of_sides <= 10:
    angle = 360 / no_of_sides
    colour_choices = ["red","blue","green","black","brown"]
    tommy.color(random.choice(colour_choices))
    for _ in range(no_of_sides):
        tommy.forward(100)
        tommy.right(angle)
    no_of_sides += 1



screen = Screen()
screen.exitonclick()