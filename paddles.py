from turtle import *

START_POS=[(350,0),(-350,0)]
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=0.7)
        self.goto(position)

    def go_up(self):
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)

    def go_down(self):
            new_y=self.ycor()-20
            self.goto(self.xcor(),new_y)
