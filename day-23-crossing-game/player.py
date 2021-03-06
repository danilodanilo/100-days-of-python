STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        if self.ycor() > 290:
            return True

    def restart(self):
        self.goto(STARTING_POSITION)

    def turtle_position(self):
        return self.turtle.pos()