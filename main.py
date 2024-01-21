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
car_list = []

def generate_car():
    for x in range(40):
        if x == 7:
            new_car = Car((-380, random.randint(-230, 230)))
            car_list.append(new_car)



game_on = True

while game_on:
    time.sleep(0.2)
    screen.update()
    generate_car()
    for cars in car_list:
        cars.move()




screen.exitonclick()