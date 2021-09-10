from turtle import Turtle, Screen

tommy = Turtle()
screen = Screen()

def moveforward():
    tommy.forward(20)


def movebackward():
    tommy.backward(20)


def moveleftside():
    tommy.left(15)


def moverightside():
    tommy.right(15)


def clearscreen():
    tommy.clear()
    tommy.penup()
    tommy.home()
    tommy.pendown()


screen.listen()
screen.onkey(key="w",fun=moveforward)
screen.onkey(key="s",fun=movebackward)
screen.onkey(key="a",fun=moveleftside)
screen.onkey(key="d",fun=moverightside)
screen.onkey(key="c",fun=clearscreen)
screen.exitonclick()