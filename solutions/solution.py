import abc

import intersection


class Solution(abc.ABC):
    def __init__(self, intersections: dict[int, intersection.Intersection], filename: str):
        self.intersections = intersections
        self.filename = filename

    @abc.abstractmethod
    def run(self) -> dict[int, intersection.Intersection]:
        ...

    def serialise(self, score: int) -> None:
        filename = self.filename.split('.')[0]
        with open(f'output/{filename}_{self.name}_{score}.out', 'w') as file:
            file.write(str(len(self.intersections)) + '\n')
            for intersection in self.intersections.values():
                file.write(str(intersection.id) + '\n')
                file.write(str(len(set(intersection.schedule))) + '\n')

                current_street: str = intersection.schedule[0]
                current_count = 1
                for scheduled_street in intersection.schedule[1:]:
                    if scheduled_street == current_street:
                        current_count += 1
                    else:
                        file.write(f'{current_street} {str(current_count)}\n')
                        current_street = scheduled_street
                        current_count = 1
                file.write(f'{current_street} {str(current_count)}\n')

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError
