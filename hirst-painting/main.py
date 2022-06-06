from typing import List, Tuple, Any
from turtle import Turtle, Screen

import random
# rgb_colors = []
# colors = colorgram.extract('paint.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle = Turtle()
color_list: list[tuple[int, int, int] | Any] = [(239, 245, 250), (250, 242, 247), (243, 251, 246), (139, 164, 184),
                                                (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89),
                                                (22, 136, 66), (139, 21, 37), (124, 72, 94), (185, 176, 26),
                                                (70, 30, 37), (182, 73, 41),
                                                (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99),
                                                (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112),
                                                (38, 37, 43), (239, 216, 8), (188, 184, 210), (158, 207, 215),
                                                (152, 214, 174), (240, 169, 154), (105, 41, 39)]
screen = Screen()
screen.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

for i in range(10):
    for k in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.forward(50)

    turtle.backward(50*10)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)

    turtle.right(90)

turtle.home()

screen.exitonclick()
