from turtle import Turtle





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("file.txt") as file:
            highscore = file.read()
        self.highscore = highscore
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score} highscore:{self.highscore}", align='center', font=('Arial', 15, 'normal'))
        self.hideturtle()

    def eaten(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} highscore:{self.highscore}", align='center', font=('Arial', 15, 'normal'))


    def changehs(self):
        if self.score > int(self.highscore):
            with open("file.txt", mode="w") as file:
                file.write(f"{self.score}")


    def loser(self):
        self.goto(0, 0)
        self.write("GAME OVER LMAO", align='center', font=('Arial', 15, 'normal'))


