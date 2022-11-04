from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left=0
        self.score_right=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50,260)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_left} SCORE {self.score_right}", font=("Verdena", 16))

    def score_left_update(self):
        self.score_left+=1
        self.clear()
        self.update_score()

    def score_right_update(self):
        self.score_right += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(-70,0)


