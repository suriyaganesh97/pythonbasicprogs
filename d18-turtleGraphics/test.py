from turtle import Turtle
from turtle import Screen


tommy = Turtle()
tommy.shape("turtle")
for i in range(4):
    tommy.forward(100)
    tommy.right(90)


screen = Screen()
screen.exitonclick()

