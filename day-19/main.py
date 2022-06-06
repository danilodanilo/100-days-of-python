from turtle import Turtle, Screen
import random

screen = Screen()

# def move_forwards():
#     turtle.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()


###Etch-a-sketch app

# screen.listen()
#
#
# def move_forwards():
#     turtle.forward(10)
#
#
# def move_backwards():
#     turtle.back(10)
#
#
# def counter_clockwise():
#     turtle.left(10)
#
#
# def clock_wise():
#     turtle.right(10)
#
#
# def clear_screen():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
#
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clock_wise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()

############################################

##### Turtle Race Game #########


screen.setup(width=500, height=400)
user1_bet = screen.textinput(title="Make your bet user 1",
                             prompt="Choose the turtle color that you thing will win the race. Enter a color")
user2_bet = screen.textinput(title="Make your bet user 2",
                             prompt="Choose the turtle color that you thing will win the race. Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -100
turtle_index: int
game_continue = True
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=-y_position)
    y_position += 30
    all_turtles.append(turtle)
while game_continue:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user1_bet:
                print(f"User 1 have won! The {winning_color} turtle is the winner!")
            elif winning_color == user2_bet:
                print(f"User 2 have won! The {winning_color} turtle is the winner!")
            else:
                print(f"Computer wins!The {winning_color} turtle is the winner!")
            game_continue = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
