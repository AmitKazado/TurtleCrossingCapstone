import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_X_AXIS = 280


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 4)

        if random_chance == 1:
            # This mechanism created in order to reduce the number of cars created
            # to keep the game on a possible playing level.
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car_y_axis = random.randint(-240, 240)
            car.penup()
            car.goto(CAR_X_AXIS, car_y_axis)
            car.shapesize(0.5, 1)
            car.setheading(180)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -290:
                car.clear()
                car.hideturtle()
                self.cars.remove(car)
