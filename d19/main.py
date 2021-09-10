from turtle import Turtle, Screen

tommy = Turtle()
screen = Screen()

def moveforward():
    tommy.forward(20)

screen.listen()
screen.onkey(key="space",fun=moveforward)
screen.exitonclick()