import street

from typing import Optional

class Car:

    def __init__(self, route: list[street.Street], current_position: int):
        self.route = route
        self.visited: list[street.Street] = []
        self.initial_position = current_position
        self.current_position = current_position

        self.route[0].cached_cars.append(self)

    def step(self, tick: int) -> None:
        self.current_position += 1

        if not self.route_complete:
            if self.current_position >= len(self.route[0]):
                if self.current_street.light_green and self.current_street.get_front_car(tick) == self:
                    old_street = self.route.pop(0)
                    self.visited.append(old_street)
                    old_street.cached_cars.remove(self)

                    self.current_position = 0

                    self.route[0].cached_cars.append(self)

    @property
    def current_street(self) -> Optional[street.Street]:
        return self.route[0] if len(self.route) else None

    @property
    def route_complete(self) -> bool:
        return len(self.route) == 1 and self.current_position >= len(self.route[0])

    def reset(self):
        self.route = self.visited + self.route
        self.visited = []
        self.current_position = self.initial_position

    def __repr__(self):
        return f'<Route: {self.route}, Time on road: {self.current_position}, Route complete: {self.route_complete}>'
