import car
import street
import intersection


class World:

    def __init__(self, filename: str, schedule: dict[int, list[str]]) -> None:
        self.streets: list[street.Street] = []
        self.cars: list[car.Car] = []

        self.duration: int = 0
        self.points_per_car: int = 0
        self.intersections: dict[int, intersection.Intersection] = {}

        self.schedule: list[tuple[str, int]] = []

        with open(f'input/{filename}', 'r') as file:
            first_line_data = file.readline().strip('\n').split(' ')
            self.duration = int(first_line_data[0])
            # intersection_count = int(first_line_data[1])
            street_count = int(first_line_data[2])
            car_count = int(first_line_data[3])
            self.points_per_car = int(first_line_data[4])

            for _ in range(street_count):
                street_data = file.readline().strip('\n').split(' ')
                street_object = street.Street(street_data[2], int(street_data[3]), self)
                self.streets.append(street_object)

                intersection_id = int(street_data[1])
                if intersection_id not in self.intersections:
                    self.intersections[intersection_id] = intersection.Intersection(intersection_id, schedule[intersection_id])
                self.intersections[intersection_id].streets.append(street_object)

            for i in range(car_count):
                car_data = file.readline().strip('\n').split(' ')
                route: list[street.Street] = []
                for route_street in car_data[1:]:
                    street_object = [s for s in self.streets if s.name == route_street][0]
                    route.append(street_object)
                self.cars.append(car.Car(route, route[0].length + i))

        print(self.simulate())

    def simulate(self) -> int:
        assert len(self.schedule)

        cars_finished = 0

        for tick in range(self.duration):
            cars_to_delete = []
            for car in self.cars:
                car.step()
                if car.route_complete:
                    cars_finished += 1
                    cars_to_delete.append(car)

            for intersection in self.intersections.values():
                intersection.step(tick)

            # '\n'.join(self.streets)

            for car in cars_to_delete:
                self.cars.remove(car)

        return cars_finished * self.points_per_car

