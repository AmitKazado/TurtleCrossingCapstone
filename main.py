import os
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE = 280
DIFFICULTY = 0.15

screen = Screen()
screen.title("Turtle Crossing Capstone")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
os.chdir(r"C:\Users\amitk\Downloads")
screen.register_shape("finish_line_flag.gif")

flag = Turtle("finish_line_flag.gif")
flag.penup()
flag.goto(0, 270)

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(DIFFICULTY)
    car_manager.move_cars()
    screen.update()

    car_manager.create_car()
    if player.ycor() == FINISH_LINE:
        # Player reached finish line is advanced to the next level, which make the cars move faster
        scoreboard.increase_score()
        player.restart_position()
        DIFFICULTY *= 0.9

    for car in car_manager.cars:
        # Collision with a car detected
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
