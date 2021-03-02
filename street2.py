import car2
import world2


class Street:

    def __init__(self, name: str, length: int, world: world2.World):
        self.length = length
        self.world = world
        self.name = name

        self.green_light = False
        self.cars: list[tuple[int, car2.Car]] = []
        self.initial_cars: list[tuple[int, car2.Car]] = []

    def add_car(self, car: car2.Car, tick: int, initial_car: bool=False):
        exit_tick = tick + self.length
        if initial_car:
            exit_tick = tick

        self.cars.append((exit_tick, car))


    def step(self, tick: int) -> int:
        """Step all cars in the simulation and return the increase in score."""
        if not self.green_light or not len(self.cars):
            return 0

        front_car = self.cars[0]
        if front_car[0] > tick:
            return 0

        del self.cars[0]

        next_street = front_car[1].next()
        if next_street:
            self.world.streets[next_street].add_car(front_car[1], tick)
            return 0

        print(f'{front_car[1]} finished at tick {tick}')
        return self.world.points_per_car + (self.world.duration - tick)

    def backup(self):
        self.initial_cars = list(self.cars)

    def reset(self):
        self.cars = list(self.initial_cars)
        self.green_light = False

    def __repr__(self):
        return f'<Name: {self.name}, Length: {self.length}, Green light: {self.green_light}, Cars: {self.cars}>'

    def __str__(self):
        return repr(self)
