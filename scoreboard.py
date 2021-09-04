

from turtle import Turtle



ALIGMENT = 'center'
FONT = ("Courier", 70 , "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.goto(-100, 230)
        self.write(self.score_l , align=ALIGMENT, font=FONT)
        self.goto(100, 230)
        self.write(self.score_r, align=ALIGMENT, font=FONT)
        '''below solution with one line :'''
        # self.write(f'{self.score_l}  :  {self.score_r}', align=ALIGMENT, font=FONT)

    def increas_point(self, point):
        if point == 'l':
            self.score_r += 1

        elif point == 'r':
            self.score_l += 1

        self.clear()
        self.updatescore()

    def game_over(self):
        self.write(f"GAME OVER !", align=ALIGMENT, font=FONT)