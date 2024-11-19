from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("black")
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    
    def plus_score(self):
        self.level += 1
        self.update_scoreboard()

        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center" ,font=FONT)