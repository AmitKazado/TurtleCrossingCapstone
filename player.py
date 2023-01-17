from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(1, 1)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def restart_position(self):
        self.goto(STARTING_POSITION)
