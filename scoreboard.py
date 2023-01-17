from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"
SCOREBOARD_POSITION = (-170, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_score()
        self.game_over_sign = Turtle()
        self.game_over_sign.color("red")
        self.game_over_sign.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.current_level}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.current_level += 1
        self.update_score()

    def game_over(self):
        self.game_over_sign.write("Game Over", False, ALIGNMENT, FONT)
