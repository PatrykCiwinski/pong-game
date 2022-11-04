import random
import time
import turtle
from turtle import *
from paddles import *
from ball import *
from scoreboard import *


my_screen=turtle.Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

paddle_r=Paddle((350,0))
paddle_l=Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(paddle_r.go_up, "Up")
my_screen.onkey(paddle_r.go_down, "Down")
my_screen.onkey(paddle_l.go_up, "w")
my_screen.onkey(paddle_l.go_down, "s")

game_on=True
while game_on:
    time.sleep(ball.speed)
    my_screen.update()
    ball.move()

#detection ball colission with up/down walls
    if ball.ycor()>290 or ball.ycor()<-290 :
        ball.bounce_y()



#detection ball collission with paddles
    if ball.distance(paddle_r)<40 and ball.xcor()>330:
        ball.bounce_x()

    if ball.distance(paddle_l)<40 and ball.xcor()<-330:
        ball.bounce_x()


#collision with right/left wall
    if ball.xcor()>390:
        scoreboard.score_left_update()
        ball.restart()

    elif ball.xcor()<-390:
        scoreboard.score_right_update()
        ball.restart()

    if scoreboard.score_left ==2:
        scoreboard.game_over()
        scoreboard.write("The winner is Left!", font=("Verdena, 18"))
        game_on=False
    elif scoreboard.score_right == 2:
        scoreboard.game_over()
        scoreboard.write("winner is right!", font=("Verdena, 18"))
        game_on = False




my_screen.exitonclick()