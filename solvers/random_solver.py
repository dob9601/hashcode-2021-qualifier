from random import shuffle, random

from solvers.solver import Solver
from world import World
from schedule import Schedule


class RandomSolver(Solver):
    name = 'random'

    def __init__(self, world: World):
        super().__init__(world)

    def generate_schedule(self) -> Schedule:
        schedule = []
        for intersection in self.world.intersections:
            streets = [s.name for s in intersection.streets]
            shuffle(streets)
            for index, current_street in enumerate(streets):
                while random() > 0.4:
                    streets.insert(index, current_street)

            schedule.append(streets)

        return Schedule(schedule)

    def run(self):
        print('-> Initiating Descent')
        best_score = 0
        for _ in range(1000):
            schedule = self.generate_schedule()
            score = self.world.simulate(schedule)
            print(score)
            if score > best_score:
                print('-> New best score found')
                best_score = score
                schedule.serialise(best_score, 'asdf', self.name)
