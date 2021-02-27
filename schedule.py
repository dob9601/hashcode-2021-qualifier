from __future__ import annotations

from intersection import Intersection


class Schedule:
    def __init__(self, data: list[list[str]]):
        self.data = data

    def get_intersection_schedule(self, intersection: Intersection):
        return self.data[intersection.id]

    def serialise(self, score: int, filename: str, solver_name: str) -> None:
        filename = filename.split('.')[0]
        with open(f'output/{filename}_{solver_name}_{score}.out', 'w') as file:
            file.write(str(len(self.data)) + '\n')
            for i, intersection in enumerate(self.data):
                file.write(str(i) + '\n')
                file.write(str(len(set(intersection))) + '\n')

                current_street: str = intersection[0]
                current_count = 1
                for scheduled_street in intersection[1:]:
                    if scheduled_street == current_street:
                        current_count += 1
                    else:
                        file.write(f'{current_street} {str(current_count)}\n')
                        current_street = scheduled_street
                        current_count = 1
                file.write(f'{current_street} {str(current_count)}\n')

    def add_intersection(self, new_intersection: Intersection, schedule: list[str]):
        self.data[new_intersection.id] = schedule

    @staticmethod
    def from_file(filename: str) -> Schedule:
        with open(f'ouput/{filename}.out','r') as file:
            intersections = int(file.readline())
            schedule = [[] for _ in range(intersections)]
            for intersection in range(intersections):
                streets = int(file.readline())
                for _ in range(streets):
                    current_street = file.readline().split(" ")
                    schedule[intersection] += [current_street[0]] * int(current_street[1])
        return Schedule(schedule)
