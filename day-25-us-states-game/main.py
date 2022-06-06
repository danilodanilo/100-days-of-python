import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# this function get the X and Y values of each state, to be used when the user enter a name and the name appear on
# the map
# def get_mouse_click_coor(x, y): print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# answer_state = screen.textinput(title="Guess a State", prompt="Type in a valid state name").lower()

data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()
length = str(len(states))
correct_answers = 0
correct_answers_list = []

while len(states) > 0:
    answer_state = screen.textinput(title=f"{str(correct_answers) + '/'+  length} Guess a State", prompt="Type in a valid state name to be plotted on the map").title()

    if answer_state in states:
        correct_answers_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_row = data[data.state == answer_state]
        states.remove(answer_state)
        pos_x = int(correct_row.x)
        pos_y = int(correct_row.y)
        t.goto(pos_x, pos_y)
        t.write(answer_state)
        correct_answers += 1
    if answer_state.lower() == "exit":
        data_frame = pandas.DataFrame(states)
        data_frame.to_csv("need_to_learn_those_states.csv")
        break
screen.exitonclick()
