from typing import Optional

import car2
import intersection2
import street2
import schedule


class World:

    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.streets: dict[str, street2.Street] = {}
        self.cars: list[car2.Car] = []

        self.duration: int = 0
        self.points_per_car: int = 0
        self.intersections: list[Optional[intersection2.Intersection]]

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
                street_object = street2.Street(street_data[2], int(street_data[3]), self)
                self.streets[street_object.name] = street_object

                intersection_id = int(street_data[1])
                if not(self.intersections[intersection_id]):
                    self.intersections[intersection_id] = intersection2.Intersection(intersection_id)
                self.intersections[intersection_id].streets.append(street_object)

            print('-> Generating Cars')
            for _ in range(car_count):
                car_data = file.readline().strip('\n').split(' ')
                new_car = car2.Car(car_data[2:])
                self.cars.append(new_car)

                self.streets[car_data[1]].add_car(new_car, 0, True)

        for s in self.streets.values():
            s.backup()
        # print(min(self.cars, key=lambda x: len(x.route)))

    def simulate(self, world_schedule: schedule.Schedule) -> int:
        for i, schedule in enumerate(world_schedule.data):
            self.intersections[i].schedule = schedule

        points = 0


        """
        active_streets = []
        for car in self.cars:
            for street in car.streets:
                street = self.streets[street]
                if street not in active_streets:
                    active_streets.append(street)
        """

        for tick in range(self.duration + 1):
            # print(self.cars[278])
            if tick % 100 == 0: print(f'{tick}/{self.duration}')

            for intersection in self.intersections:
                intersection.step(tick)

            # print(len(self.streets['dif-dig'].cars))

            for street in self.streets.values(): #active_streets
                points += street.step(tick)

        for current_car in self.cars:
            current_car.reset()

        for current_street in self.streets.values():
            current_street.reset()


        return points
