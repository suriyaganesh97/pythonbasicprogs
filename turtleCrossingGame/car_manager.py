from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle("square")
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.new_y = random.randint(-250, 250)
            new_car.new_x = 300
            new_car.goto(new_car.new_x, new_car.new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT