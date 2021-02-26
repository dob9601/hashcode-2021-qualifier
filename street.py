from __future__ import annotations

import world
import car


class Street:

    def __init__(self, name: str, length: int, world: world.World):
        self.length = length
        self.name = name
        self.world = world

        self.light_green = True

    @property
    def cars(self) -> list[car.Car]:
        return [car for car in self.world.cars if car.current_street == self]

    @property
    def front_car(self) -> car.Car:
        return max(self.cars, key=lambda car: car.current_position)

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'<Name: {self.name}, Length: {self.length}, Green light: {self.light_green}>'

    def __str__(self):
        return repr(self)

    '''def __eq__(self, other: Street):
        return self.name == other.name and self.length == other.length'''
