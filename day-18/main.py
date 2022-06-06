from turtle import Turtle, Screen
import random

the_turtle = Turtle()
screen = Screen()
the_turtle.shape("turtle")
screen.colormode(255)
colours = ["green", "firebrick", "magenta", "navy", "black", "medium turquoise", "light gray", "goldenrod", "sienna",
           "medium violet red"]
direction = [0, 90, 180, 360]


### Code below draws in the interface multiple shapes, from a triangle to a decagon ###
# while_control = 5
# count = 3
# while while_control >= 0:
#     angle = 360/count
#
#     the_turtle.pencolor(random.choice(colours))
#     for _ in range(count):
#
#         the_turtle.forward(100)
#         the_turtle.right(angle)
#     count += 1
#     while_control -= 1
###

### Random Walk challenge plus random color ###

def generate_color_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


#
#
# the_turtle.pensize(20)
# the_turtle.speed("fastest")
#
# for _ in range(200):
#     the_turtle.forward(50)
#     the_turtle.color(generate_color_random())
#     the_turtle.setheading(random.choice(direction))
###

###Draw a Spirograph###
the_turtle.speed("fastest")
for _ in range(360):
    the_turtle.color(generate_color_random())
    the_turtle.circle(100)
    the_turtle.left(5)

screen = Screen()
screen.exitonclick()

####
