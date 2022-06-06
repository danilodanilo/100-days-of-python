import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(turtle.up, "Up")
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_new_car()
    car.move_forward()

    #detect collision with  finish line
    if turtle.check_finish_line():
        scoreboard.increase_score()
        car.level_up()
        turtle.restart()

    #detect collision with car
    for n_car in car.cars:
        if n_car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
