from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt = "which turetle will win the race, enter the colour")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_position = 0
for i in range(6):
    tommy = Turtle(shape="turtle")
    tommy.penup()
    tommy.color(colors[i])
    tommy.goto(x=-230, y=(-90 + y_position))
    y_position += 30
    all_turtles.append(tommy)


is_game_on = False
if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        move_forward = random.randint(0,10)
        turtle.forward(move_forward)
        if turtle.xcor() > 230:
            is_game_on = False
            winner_turtle = turtle.pencolor()
            if user_bet == winner_turtle:
                print(f"you won, the winner is {winner_turtle}")
            else:
                print(f"you lost, the winner is {winner_turtle}")



screen.exitonclick()