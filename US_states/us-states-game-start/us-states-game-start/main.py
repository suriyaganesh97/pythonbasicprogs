from turtle import Turtle
import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
correct_guess = 0
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
state_list = data["state"].to_list()
correct_guess_list = []
is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"state names {correct_guess}/50", prompt=f"enter a state name:")
    answer = answer_state.title()
    for state in state_list:
        if state == answer:
            correct_guess += 1
            state_data = data[data.state == answer]
            x_cor = int(state_data.x)
            y_cor = int(state_data.y)
            turtle.goto(x_cor, y_cor)
            turtle.write(answer)
            correct_guess_list.append(answer)
    if correct_guess == 50:
        is_game_on = False
    if answer == "Exit":
        missing_states = []
        for states in state_list:
            if states not in correct_guess_list:
                missing_states.append(states)
        #print(missing_states)
        is_game_on = False
new_data_state = pandas.DataFrame(missing_states)
new_data_state.to_csv("statesToLearn.csv")
#screen.exitonclick()