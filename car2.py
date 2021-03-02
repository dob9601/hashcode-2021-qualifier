from typing import Optional


class Car:

    def __init__(self, streets: list[str]) -> None:
        self.streets = streets
        self.visited = []

    def next(self) -> Optional[str]:
        if not len(self.streets):
            return None

        street = self.streets.pop(0)
        self.visited.append(street)
        return street

    @property
    def route_complete(self):
        return not len(self.streets)

    def reset(self):
        self.streets = self.visited + self.streets
        self.visited = []

    def __repr__(self):
        return f'<Route: {self.streets}, Visited: {self.visited}, Route complete: {self.route_complete}>'
