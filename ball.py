
from turtle import Turtle, Screen



class Ball(Turtle):
    
    def __init__(self):
        # super().__init__()
        Turtle.__init__(self)
        self.x_ball = 10
        self.y_ball = 10
        self.shape("circle")
        self.penup()
        self.color('yellow')
        self.ball_move()
        self.ball_speed = 0.1

    def ball_move(self):

        x_ball_pos = self.xcor() + self.x_ball
        y_ball_pos = self.ycor() + self.y_ball
        self.goto(x_ball_pos, y_ball_pos)
        print(f' x {self.x_ball} y {self.y_ball}')
        # self.goto(0,0)

    def ball_wall_bounce(self):
        self.y_ball *= -1


    def bounce_from_paddle(self):
        # self.x_ball *= 1.15  # ball speed increase
        # self.y_ball *= 1.15  # ball speed increase
        self.x_ball *= -1
        self.ball_speed *= 0.7

    def reset_ball_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        print(f' x {self.x_ball} y {self.y_ball}')
        self.x_ball *= -1














