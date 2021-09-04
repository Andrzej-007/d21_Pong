

from turtle import Turtle


ALIGMENT = 'center'
FONT = ("Arial", 35 , "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.color('white')
        self.goto(-5, 260)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f'{self.score_l}  :  {self.score_r}', align=ALIGMENT, font=FONT)

    def increas_point(self, point):
        if point == 'l':
            self.score_r += 1
        elif point == 'r':
            self.score_l += 1

        self.clear()
        self.updatescore()

