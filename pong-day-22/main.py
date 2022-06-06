from turtle import Screen
from bar import Bars
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = ScoreBoard()
left_bar = Bars((-380, 0))
right_bar = Bars((380, 0))
ball = Ball()
screen.listen()
screen.onkeypress(left_bar.go_up, "w")
screen.onkeypress(left_bar.go_down, "s")
screen.onkeypress(right_bar.go_up, "Up")
screen.onkeypress(right_bar.go_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(ball.game_velocity)
    screen.update()
    ball.ball_move()
    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce()
    # detect collision with the paddle
    if ball.distance(right_bar) < 50 and ball.xcor() > 320 or ball.distance(left_bar) < 50 and ball.xcor() < -320:
        ball.bounce_from_paddle()

    # detect when paddle misses the ball
    if ball.xcor() > 390:
        ball.restart()
        scoreboard.increment_l_score()
    if ball.xcor() < -390:
        scoreboard.increment_r_score()
        ball.restart()
screen.exitonclick()
