"""Street module."""
from __future__ import annotations
from typing import NamedTuple, Optional

import world
import car


class Street:
    """Class representing a street."""

    class CachedFrontCar(NamedTuple):
        """Named tuple used to cache the front car on the street."""

        tick: int
        front_car: Optional[car.Car]

    def __init__(self, name: str, length: int, sim_world: world.World):
        """Initialise the street with a given name and length, store a ref to the world object."""
        self.length = length
        self.name = name
        self.world = sim_world

        self.schedule: list[bool] = []

        self.cached_front_car = Street.CachedFrontCar(0, None)
        self.cached_cars: list[car.Car] = []

    def set_schedule(self, intersection_schedule: list[str]):
        """Initialise the traffic light schedule from a list of strings."""
        self.schedule = [item == self.name for item in intersection_schedule]

    def is_light_green(self, tick: int):
        """Return whether the traffic light is a green on a given tick."""
        return self.schedule[tick % len(self.schedule)]

    @property
    def cars(self) -> list[car.Car]:
        return self.cached_cars

    def get_front_car(self, tick: int) -> car.Car:
        if self.cached_front_car.tick == tick and self.cached_front_car.front_car is not None:
            return self.cached_front_car.front_car

        front_car = self.cached_cars[0]
        self.cached_front_car = Street.CachedFrontCar(tick, front_car)

        return front_car

    def reset(self):
        """Reset the street to factory state."""
        self.cached_cars = []
        self.cached_front_car = Street.CachedFrontCar(0, None)

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'<Name: {self.name}, Length: {self.length}, Schedule: {self.schedule}>'

    def __str__(self):
        return repr(self)
