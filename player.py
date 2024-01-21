from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.goto(0, -240)
        self.showturtle()

    def up(self):
        self.forward(5)



