from random import shuffle, random
import os

import car
import intersection
import street


class World:

    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.streets: list[street.Street] = []
        self.cars: list[car.Car] = []

        self.duration: int = 0
        self.points_per_car: int = 0
        self.intersections: dict[int, intersection.Intersection] = {}

        print('Generating world')
        with open(f'input/{filename}', 'r') as file:
            first_line_data = file.readline().strip('\n').split(' ')
            self.duration = int(first_line_data[0])
            # intersection_count = int(first_line_data[1])
            street_count = int(first_line_data[2])
            car_count = int(first_line_data[3])
            self.points_per_car = int(first_line_data[4])

            print('-> Generating Streets')
            for _ in range(street_count):
                street_data = file.readline().strip('\n').split(' ')
                street_object = street.Street(street_data[2], int(street_data[3]), self)
                self.streets.append(street_object)

                intersection_id = int(street_data[1])
                if intersection_id not in self.intersections:
                    self.intersections[intersection_id] = intersection.Intersection(intersection_id)
                self.intersections[intersection_id].streets.append(street_object)

            print('-> Generating Cars')
            for i in range(car_count):
                car_data = file.readline().strip('\n').split(' ')
                route: list[street.Street] = []
                for route_street in car_data[1:]:
                    street_object = [s for s in self.streets if s.name == route_street][0]
                    route.append(street_object)
                self.cars.append(car.Car(route, route[0].length + i))

        self.descend()

    def simulate(self) -> int:
        print('-> Duplicating Cars and Intersections')
        intersections = self.intersections.copy()

        points = 0

        print('Running Solution')
        for tick in range(self.duration):
            if tick % 100 == 0:
                print(f'-> Step {tick}/{self.duration}', end='\r')
            for current_car in self.cars:
                if not current_car.route_complete:
                    current_car.step()
                    if current_car.route_complete:
                        points += self.points_per_car + (self.duration - tick)

            for intersection in intersections.values():
                intersection.step(tick)

        print('\n-> Restoring initial state')
        for current_car in self.cars:
            current_car.reset()

        for current_street in self.streets:
            current_street.reset()

        return points

    def descend(self):
        print('-> Initiating Descent')
        best_score = 0
        for _ in range(1000):
            self.generate_schedule()
            score = self.simulate()
            print(score)
            if score > best_score:
                print('-> New best score found')
                best_score = score
                self.serialise(best_score)

    def generate_schedule(self) -> None:
        for intersection in self.intersections.values():
            streets = [s.name for s in intersection.streets]
            shuffle(streets)
            for index, current_street in enumerate(streets):
                while random() > 0.7:
                    streets.insert(index, current_street)

            intersection.schedule = streets
