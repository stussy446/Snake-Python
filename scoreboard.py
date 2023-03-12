from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game Over, Final Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
