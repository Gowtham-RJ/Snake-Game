import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))