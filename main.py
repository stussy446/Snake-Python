import turtle
from turtle import Screen
from snake import Snake
from food import Food
import time


def setup_screen(start_screen: Screen):
    start_screen.setup(width=600, height=600)
    start_screen.bgcolor('black')
    start_screen.title("Snake")
    screen.tracer(0)


def set_key_bindings():
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)


# DRIVER CODE
screen = Screen()
game_is_on = True

setup_screen(screen)
snake = Snake()
food = Food()
screen.listen()
set_key_bindings()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.go_to_random_location()

screen.exitonclick()
