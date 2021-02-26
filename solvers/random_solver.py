from random import shuffle

from solvers.solver import Solver
from world import World


class RandomSolver(Solver):
    name = 'random'

    def __init__(self, world: World):
        super().__init__(world)

    def generate_schedule(self) -> None:
        for intersection in self.intersections:
            streets = [s.name for s in intersection.streets]
            shuffle(streets)
            for index, current_street in enumerate(streets):
                while random() > 0.7:
                    streets.insert(index, current_street)

            intersection.schedule = streets
