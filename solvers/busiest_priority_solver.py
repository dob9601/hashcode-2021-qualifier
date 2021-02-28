from solvers.solver import Solver
from world import World
from schedule import Schedule


class BusiestPrioritySolver(Solver):
    name = 'bps'

    def __init__(self, world: World):
        super().__init__(world)

    def run(self):
        print('Generating Solution')
        street_weighting: dict[str, float] = {}
        for car in self.world.cars:
            for street in car.route:
                if street.name not in street_weighting:
                    street_weighting[street.name] = 1.0
                else:
                    street_weighting[street.name] += 0.1

        schedule = []
        for intersection in self.world.intersections:
            streets = []
            for s in intersection.streets:
                for _ in range(round(street_weighting.get(s.name, 0))):
                    streets.append(s.name)

            if not len(streets):
                streets.append(intersection.streets[0].name)

            schedule.append(streets)

        schedule = Schedule(schedule)
        score = self.world.simulate(schedule)
        print(f'-> Score: {score}')
        schedule.serialise(score, self.world.filename, self.name)
