from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_POSITION = 350, 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('green')
screen.title(titlestring="Pang Game")
screen.tracer(0)


middle_line = Turtle(shape="square")
middle_line.hideturtle()
middle_line.speed("fastest")
middle_line.penup()
middle_line.goto(x=0, y=300)
middle_line.setheading(270)
# middle_line.color("red")
middle_line.pen(fillcolor="red", pencolor="red", pensize=10)


while True:
    middle_line.pendown()
    middle_line.forward(30)
    middle_line.penup()
    middle_line.forward(20)
    if middle_line.ycor() < -300:
        break


paddle_r = Paddle(350,0)
paddle_l = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()

    # ball bounce form wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.ball_wall_bounce()

    # ball bounce form paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330:
        ball.bounce_from_paddle()
    if paddle_l.distance(ball) < 50 and  ball.xcor() < -330:
        ball.bounce_from_paddle()

    # detect  R scoure and reset position
    if ball.xcor() > 380 :
        ball.reset_ball_position()
        scoreboard.increas_point('r')

    # detect  R scoure and reset position
    if ball.xcor() < -380 :
        ball.reset_ball_position()
        scoreboard.increas_point('l')



screen.exitonclick()