import random

from solvers.solver import Solver
from world import World
from schedule import Schedule

class ReorderOptimiser(Solver):
    name = 'ro'
    epochs = 1000
    mutativity = 0.1

    class EvaluatedSchedule():
        def __init__(self, schedule: Schedule, score: int = 0):
            self.schedule = schedule
            self.score = score

    def __init__(self, world: World, schedule: Schedule):
        super().__init__(world)
        self.schedule = schedule

    def run(self):
        initial_score = self.world.simulate(self.schedule)
        best_schedule = self.EvaluatedSchedule(self.schedule, initial_score)
        for i in range(1000):
            print(f'Epoch {i+1}/1000')

            new_schedule_data = []
            for street_schedule in best_schedule.schedule.data:
                if random.random() < self.mutativity:
                    streets = list(set(street_schedule))
                    random.shuffle(streets)
                    new_data = []
                    for s in streets:
                        new_data += [s] * len([i for i in street_schedule if i == s])
                    new_schedule_data.append(new_data)
                else:
                    new_schedule_data.append(list(street_schedule))

            new_schedule = Schedule(new_schedule_data)
            new_score = self.world.simulate(new_schedule)
            if new_score > best_schedule.score:
                print(f'New Best Schedule | Score: {new_score}')
                best_schedule = self.EvaluatedSchedule(new_schedule, new_score)
                best_schedule.schedule.serialise(best_schedule.score, self.world.filename, self.name)
            else:
                print(f'Score: {new_score}')
