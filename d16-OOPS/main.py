# from turtle import Turtle, Screen
# tommy = Turtle() #creating an object called tommy
# print(tommy)
# tommy.shape("turtle")
# tommy.color("red")
# tommy.forward(100)
# #Turtle, Screen both of this are classes so named in Pascal case
# #tommy and my_screen are objects created
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["electric","water","fire"])
table.align="l"
print(table)