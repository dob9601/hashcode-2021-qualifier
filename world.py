from typing import Optional

import car
import intersection
import street
import schedule


class World:

    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.streets: dict[str, street.Street] = {}
        self.cars: list[car.Car] = []

        self.duration: int = 0
        self.points_per_car: int = 0
        self.intersections: list[Optional[intersection.Intersection]]

        print('Generating world')
        with open(f'input/{filename}', 'r') as file:
            first_line_data = file.readline().strip('\n').split(' ')
            self.duration = int(first_line_data[0])
            self.intersection_count = int(first_line_data[1])
            self.intersections = [None for _ in range(self.intersection_count)]
            street_count = int(first_line_data[2])
            car_count = int(first_line_data[3])
            self.points_per_car = int(first_line_data[4])

            print('-> Generating Streets')
            for _ in range(street_count):
                street_data = file.readline().strip('\n').split(' ')
                street_object = street.Street(street_data[2], int(street_data[3]), self)
                self.streets[street_object.name] = street_object

                intersection_id = int(street_data[1])
                if not(self.intersections[intersection_id]):
                    self.intersections[intersection_id] = intersection.Intersection(intersection_id)
                self.intersections[intersection_id].streets.append(street_object)

            print('-> Generating Cars')
            for i in range(car_count):
                car_data = file.readline().strip('\n').split(' ')
                route: list[street.Street] = []
                for route_street in car_data[1:]:
                    street_object = self.streets[route_street]
                    route.append(street_object)
                self.cars.append(car.Car(route, route[0].length + i))

    def simulate(self, world_schedule: schedule.Schedule) -> int:
        print(len(self.cars))
        for current_car in self.cars:
            current_car.reset()

        for current_street in self.streets.values():
            current_street.reset()
        # print('-> Duplicating Intersections')
        intersections = self.intersections.copy()

        for i, schedule in enumerate(world_schedule.data):
            intersections[i].schedule = schedule

        points = 0

        # print('Running Solution')
        for tick in range(self.duration):
            # if tick % 100 == 0:
                # print(f'-> Step {tick}/{self.duration}', end='\r')
            for current_car in self.cars:
                if not current_car.route_complete:
                    current_car.step()
                    if current_car.route_complete:
                        points += self.points_per_car + (self.duration - tick)

                    #print(current_car)

            for intersection in intersections:
                intersection.step(tick)

            # breakpoint()

        # print('\n-> Restoring initial state')
        for current_car in self.cars:
            current_car.reset()

        for current_street in self.streets.values():
            current_street.reset()

        return points
