import time
from turtle import Turtle, Screen
from snake import Snake
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

# turtle_list = []
# original_pos = 0
# for i in range(3):
#     turtle = Turtle()
#     turtle.penup()
#     turtle.color("white")
#     turtle.shape("square")
#     turtle_list.append(turtle)
#     turtle_list[i].backward(20 + original_pos)
#     original_pos += 20