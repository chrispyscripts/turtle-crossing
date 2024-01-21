from turtle import Screen
from player import Player
from cars import Car
import time
import random

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("grey")
screen.listen()
player = Player()
screen.onkey(player.up, "Up")
positions =


car = Car()
game_on = True

while game_on:
    time.sleep(0.2)
    screen.update()
    car.move()




screen.exitonclick()