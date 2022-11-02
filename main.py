import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width = 600, height =600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")


snake = Snake()
food = Food()
score = Score()

screen.listen()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        snake.refresh()
        score.start_over()
        snake = Snake()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<5:
            snake.refresh()
            score.start_over()
            snake = Snake()
























screen.exitonclick()

