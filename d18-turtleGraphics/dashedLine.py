from turtle import Turtle
from turtle import Screen


tommy = Turtle()
tommy.shape("turtle")
for i in range(10):
    tommy.forward(10)
    tommy.penup()
    tommy.forward(10)
    tommy.pendown()


screen = Screen()
screen.exitonclick()