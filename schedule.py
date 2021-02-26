from intersection import Intersection


class Schedule:
    def __init__(self, data: list[list[str]]):
        self.data = data

    def get_intersection_schedule(self, intersection: Intersection):
        return self.data[intersection.id]
