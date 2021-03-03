import random

from solvers.solver import Solver
from world2 import World
from schedule import Schedule
import redis
import pickle

class GeneticSolver(Solver):
    name = 'gs'
    epochs = 1000
    population = 252
    mutativity = 0.005

    class EvaluatedSchedule():
        def __init__(self, schedule: Schedule, score=0):
            self.schedule = schedule
            self.score = score

    def __init__(self, world: World):
        super().__init__(world)

    def generate_random_schedule(self) -> Schedule:
        schedule = []
        for intersection in self.world.intersections:
            streets = [s.name for s in intersection.streets]
            random.shuffle(streets)
            for index, current_street in enumerate(streets):
                while random.random() > 0.6:
                    streets.insert(index, current_street)

            schedule.append(streets)

        return Schedule(schedule)

    def breed_schedules(self, schedules: list[EvaluatedSchedule]) -> list[EvaluatedSchedule]:
        assert len(schedules) % 2 == 0

        output: list[GeneticSolver.EvaluatedSchedule] = []
        middle_index = len(schedules) // 2

        random.shuffle(schedules)
        schedules_a = schedules[:middle_index]
        schedules_b = schedules[middle_index:]
        for schedule_a, schedule_b in zip(schedules_a, schedules_b):
            for _ in range(2):
                new_schedule_data: list[list[str]] = []

                for intersection_a, intersection_b in zip(schedule_a.schedule.data, schedule_b.schedule.data):
                    new_schedule_data.append(random.choice([intersection_a, intersection_b]))

                new_schedule = Schedule(new_schedule_data)
                evaluated_schedule = self.EvaluatedSchedule(new_schedule)
                output.append(evaluated_schedule)
            output += [schedule_a, schedule_b]

        return output

    def mutate_schedules(self, schedules: list[EvaluatedSchedule]) -> list[EvaluatedSchedule]:
        output = []
        for schedule in schedules:
            mutated_schedule_data: list[list[str]] = []
            for intersection in schedule.schedule.data:
                mutated_intersection_data: list[str] = []

                for intersection_street in intersection:
                    mutation_factor = random.random()

                    if mutation_factor < self.mutativity:
                        pass
                    elif self.mutativity <= mutation_factor <= 2*self.mutativity:
                        mutated_intersection_data += [intersection_street] * 2
                    else:
                        mutated_intersection_data.append(intersection_street)

                mutated_schedule_data.append(mutated_intersection_data)

            output.append(self.EvaluatedSchedule(Schedule(mutated_schedule_data)))

        return output

    def run(self, schedules: list[EvaluatedSchedule]):
        max_score: int = 0

        red = redis.Redis("192.168.0.34", port=6379, db=0)
        red.set("world", self.world.filename)
        red.delete("tasks")
        red.delete("results")

        print(f'Commencing {self.epochs} epochs')
        for i in range(self.epochs):
            print(f'-> Epoch {i+1}/{self.epochs}')

            schedule_count = len(schedules)
            # for j, schedule in enumerate(schedules):
            #     print(f'--> Evaluating Schedule {j+1}/{schedule_count}', end='\r')
            #     score = self.world.simulate(schedule.schedule)
            #     schedule.score = score
            # print()

            # send out schedules to be processed
            for j, schedule in enumerate(schedules):
                red.rpush("tasks", pickle.dumps((j,schedule.schedule)))


            # receive preocessed schedules
            print(f'--> Receiving results 0/{schedule_count}', end='\r')
            for i in range(schedule_count):
                item = red.blpop("results",0)
                item = item[1].decode()
                item = item.split(" ")
                print(f'--> Receiving results {i}/{schedule_count} [Result {item[0]} received with score {item[1]}]             ', end='\r')
                schedules[int(item[0])].score = int(item[1])


            best_schedule = max(schedules, key=lambda x: x.score)
            print(f"--> best of epoch {best_schedule.score}")
            if best_schedule.score > max_score:
                print('--> Serialising New Best Schedule', end='')
                max_score = best_schedule.score
                best_schedule.schedule.serialise(best_schedule.score, self.world.filename, self.name)
                print(f' [DONE] [SCORE: {best_schedule.score}]')

            print('Culling, Breeding, and Mutating Schedules', end='')
            schedules.sort(key=lambda x: x.score)
            schedules = schedules[len(schedules)//2:]
            schedules = self.breed_schedules(schedules)
            schedules = self.mutate_schedules(schedules)
            print(' [DONE]')

        print(f'Best score: {max_score}')

    def run_from_existing(self, filename: str) -> None:
        schedules: list[GeneticSolver.EvaluatedSchedule] = [self.EvaluatedSchedule(Schedule.from_file(filename)) for _ in range(self.population)]
        self.run(self.mutate_schedules(schedules))


    def run_from_random(self) -> None:
        schedules: list[GeneticSolver.EvaluatedSchedule] = []

        print('Generating Population')
        for i in range(self.population):
            print(f'-> Schedule {i+1}/{self.population}', end='\r')
            schedules.append(self.EvaluatedSchedule(self.generate_random_schedule()))
        print()




