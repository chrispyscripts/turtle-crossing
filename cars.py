from turtle import Turtle

COLORS = ["red", "blue", "yellow", "black", "white"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()

    def generate(self, position):
        self.goto(position)

    def move(self):
        self.forward(10)