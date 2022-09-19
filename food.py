
from turtle import Turtle
import random

class Food(Turtle):
      #make food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))


