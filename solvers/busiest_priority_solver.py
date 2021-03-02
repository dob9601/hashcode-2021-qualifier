from solvers.solver import Solver
from world import World
from schedule import Schedule

from math import ceil


class BusiestPrioritySolver(Solver):
    name = 'bps'

    def __init__(self, world: World):
        super().__init__(world)

    def run(self):
        print('Generating Solution')
        street_weighting: dict[str, int] = {}
        for car in self.world.cars:
            for street in car.route:
                if street.name not in street_weighting:
                    street_weighting[street.name] = 1
                else:
                    street_weighting[street.name] += 1

        schedule = []
        for intersection in self.world.intersections:
            total = 0
            streets = []
            for s in intersection.streets:
                total += street_weighting.get(s.name, 0)
            total += 1

            for s in intersection.streets:
                for _ in range((ceil(street_weighting.get(s.name, 0) / total))):
                    streets.append(s.name)

            if not len(streets):
                streets.append(intersection.streets[0].name)

            schedule.append(streets)

        schedule = Schedule(schedule)
        score = self.world.simulate(schedule)
        print(f'-> Score: {score}')
        schedule.serialise(score, self.world.filename, self.name)
