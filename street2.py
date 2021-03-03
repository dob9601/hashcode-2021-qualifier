from typing import NamedTuple, Optional

import car2
import world2


class Street:

    class ActiveCar(NamedTuple):
        car: car2.Car
        exit_tick: int


    def __init__(self, name: str, length: int, world: world2.World):
        self.length = length
        self.world = world
        self.name = name

        self.green_light = False
        self.cars: list[Street.ActiveCar] = []
        self.initial_cars: list[Street.ActiveCar] = []

    def add_car(self, car: car2.Car, tick: int, initial_car: bool=False):
        exit_tick = tick + self.length
        if initial_car:
            exit_tick = tick

        self.cars.append(Street.ActiveCar(car, exit_tick))


    def step(self, tick: int) -> int:
        """Step all cars in the simulation and return the increase in score."""
        if not self.front_car or self.front_car.exit_tick > tick:
            # Either there are no cars present on the street, or no cars are currently
            # in need of moving therefore no score increase
            return 0

        delta_score = 0
        for car in self.cars:
            if not len(car.car.streets) and car.exit_tick == tick:
                self.cars.remove(car)
                delta_score += self.world.points_per_car + (self.world.duration - tick)

        if delta_score:
            return delta_score

        if self.green_light:
            # A car needs to be moved and the light is green
            next_street = self.front_car.car.streets.pop(0)
            self.world.streets[next_street].add_car(self.front_car.car, tick)
            del self.cars[0]
            return 0

        # A car needs to be moved, but the light is red therefore do nothing
        return 0

    def backup(self):
        self.initial_cars = list(self.cars)

    def reset(self):
        self.cars = list(self.initial_cars)
        self.green_light = False

    @property
    def front_car(self) -> Optional[ActiveCar]:
        return self.cars[0] if len(self.cars) else None

    def __repr__(self):
        return f'<Name: {self.name}, Length: {self.length}, Green light: {self.green_light}, Cars: {self.cars}>'

    def __str__(self):
        return repr(self)
