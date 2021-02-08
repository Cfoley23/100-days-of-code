from turtle import Turtle

FONT = ("Courier", 24, "bold")

# keeps track of the level the player is on, as well as the game over sequence
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.pu()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)