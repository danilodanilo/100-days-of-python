from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Fabulous Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        snake.extend_snake_body()
        scoreboard.increase_score()
        food.create_new_food()
    # detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    # detect collison with tail
    for segment in snake.segments[1:]:  # slice removing the head of the snake
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
