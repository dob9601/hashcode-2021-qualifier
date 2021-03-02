import street

from typing import Optional

class Car:

    def __init__(self, route: list[street.Street], current_position: int):
        self.route = route
        self.visited: list[street.Street] = []
        self.initial_position = current_position
        self.current_position = current_position

    def step(self) -> None:
        self.current_position += 1

        if not self.route_complete:
            if self.current_position > len(self.route[0]):
                if self.current_street.light_green and self.current_street.front_car == self:
                    self.visited.append(self.route.pop(0))
                    self.current_position = 1

    @property
    def current_street(self) -> Optional[street.Street]:
        return self.route[0] if len(self.route) else None

    @property
    def route_complete(self) -> bool:
        return not len(self.route)

    def reset(self):
        self.route = self.visited + self.route
        self.visited = []
        self.current_position = self.initial_position

    def __repr__(self):
        return f'<Route: {self.route}, Time on road: {self.current_position}, Route complete: {self.route_complete}>'
