
from turtle import Turtle, Screen

screen  = Screen()

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

    def ball_move(self):

        x_ball_pos = self.xcor() + self.x_ball
        y_ball_pos = self.ycor() + self.y_ball
        self.goto(x_ball_pos, y=y_ball_pos)

        if y_ball_pos > 280 or y_ball_pos < -270:
            self.y_ball *= -1

        # if y_ball_pos > 278
        #     self.y_ball = -10
        #     print(self.y_ball)
        #
        # if y_ball_pos < -270:
        #     self.y_ball = 10
        #     print(self.y_ball)


    def bounce_from_paddle(self):
        self.x_ball *= -1
        self.ball_move()


    # def paddle_right_update(self):
    #     self.x_ball = -5
    #     self.ball_move()
    #
    # def paddle_left_update(self):
    #     self.x_ball = 5
    #     self.ball_move()












