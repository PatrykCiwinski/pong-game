from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.move_x=10
        self.move_y=10
        self.speed=0.1

    def create(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 0)


    def move(self):
        new_x=self.xcor()+self.move_x
        new_y=self.ycor()+self.move_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.move_y *= -1
        self.speed*=0.9

    def bounce_x(self):
        self.move_x *= -1
        self.speed*=0.9

    def restart(self):
        self.create()
        self.speed=0.1
        self.bounce_x()





