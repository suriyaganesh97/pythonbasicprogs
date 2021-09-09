# import colorgram
#
# colors = colorgram.extract('artimage.jpg', 30)
# rgb_color_list= []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colour = (r,g,b)
#     rgb_color_list.append(rgb_colour)
#
# print(rgb_color_list)

import turtle
from turtle import Turtle
from turtle import Screen
import random
tommy = Turtle()
tommy = turtle.Turtle()
turtle.colormode(255)
tommy.speed(0)
color_list = [(152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
tommy.setheading(225)
tommy.forward(300)
tommy.setheading(0)
#print(type(random.choice(color_list)))
for i in range(100):
    tommy.dot(20, random.choice(color_list))
    #tommy.penup()
    tommy.forward(50)
    #tommy.pendown()
    if i % 10 == 0:
        tommy.setheading(90)
        tommy.forward(50)
        tommy.setheading(180)
        tommy.forward(500)
        tommy.setheading(0)
        # tommy.forward(50)
        # tommy.left(90)
        # #tommy.penup()
        # tommy.forward(50)
        # tommy.left(90)
        # tommy.forward(50)







screen = Screen()
screen.exitonclick()