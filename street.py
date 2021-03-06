from __future__ import annotations
from typing import NamedTuple, Optional

import world
import car


class Street:
    class CachedFrontCar(NamedTuple):
        tick: int
        front_car: Optional[car.Car]

    def __init__(self, name: str, length: int, world: world.World):
        self.length = length
        self.name = name
        self.world = world

        self.schedule: list[bool] = []
        self.light_green = False

        self.cached_front_car = Street.CachedFrontCar(0, None)
        self.cached_cars: list[car.Car] = []

    def set_schedule(self, intersection_schedule: list[str]):
        self.schedule = [item == self.name for item in intersection_schedule]

    def is_light_green(self, tick: int):
        return self.schedule[tick%len(self.schedule)]

    @property
    def cars(self) -> list[car.Car]:
        return self.cached_cars

    def get_front_car(self, tick: int) -> car.Car:
        if self.cached_front_car.tick == tick and self.cached_front_car.front_car is not None:
            return self.cached_front_car.front_car

        front_car = max(self.cars, key=lambda car: car.current_position)
        self.cached_front_car = Street.CachedFrontCar(tick, front_car)

        return front_car

    def reset(self):
        self.light_green = False

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'<Name: {self.name}, Length: {self.length}, Green light: {self.light_green}>'

    def __str__(self):
        return repr(self)

