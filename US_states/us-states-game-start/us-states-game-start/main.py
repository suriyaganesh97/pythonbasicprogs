import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
correct_guess = 0
answer_state = screen.textinput(title="state name", prompt="enter a state name:")
new_data = data["state"].str.contains(answer_state)
# if data["state"].str.contains(answer_state):
#     correct_guess += 1
print(new_data)

#screen.exitonclick()