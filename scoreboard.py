from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1

    
    def update_scoreboard(self):
            self.clear()
            self.goto(-220,265)
            self.write(f"Level {self.score}", align="center", font=FONT)

    def level_up(self):
         self.clear()
         self.score += 1
         self.goto(-220,265)
         self.write(f"Level {self.score}", align="center", font=FONT)

    def game_over(self):
         self.clear()
         self.goto(0,0)
         self.write(f"GAME OVER, you reached level {self.score}", align="center", font=FONT)

            