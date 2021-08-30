
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        # self.paddle_positions = pos_y   #
        # self.paddle = Turtle(shape="square")  <--- Turtle is in a class that's inherit
        # self.paddle.penup()
        # self.paddle.color("white")
        # self.paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        # self.paddle.goto(x=pos_x, y=pos_y)

        self.shape('square')
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.goto(x=pos_x, y=pos_y)


    def up(self):
        self.position_y = self.ycor() + 20
        self.setpos(self.xcor(), self.position_y)

    def down(self):
        self.position_y  = self.ycor() - 20
        self.setpos(self.xcor(), self.position_y)

