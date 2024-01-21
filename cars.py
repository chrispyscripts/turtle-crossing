from turtle import Turtle

COLORS = ["red", "blue", "yellow", "black", "white"]

class Car(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.showturtle()


    def move(self):
        self.forward(10)