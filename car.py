import street

from typing import Optional

class Car:

    def __init__(self, route: list[street.Street]):
        self.route = route
        self.visited: list[street.Street] = []

        self.exit_tick = 0
        self.update_initial_street()


    def update_initial_street(self):
        self.route[0].cached_cars.append(self)

    def step(self, tick: int) -> None:
        if not self.is_route_complete(tick):
            if tick >= self.exit_tick:
                if self.current_street.is_light_green(tick) and self.current_street.get_front_car(tick) == self:
                    old_street = self.route.pop(0)
                    self.visited.append(old_street)
                    old_street.cached_cars.remove(self)

                    self.route[0].cached_cars.append(self)
                    self.exit_tick = tick + len(self.route[0])

    @property
    def current_street(self) -> Optional[street.Street]:
        return self.route[0] if len(self.route) else None

    def is_route_complete(self, tick: int) -> bool:
        return len(self.route) == 1 and self.exit_tick <= tick

    def reset(self):
        self.route = self.visited + self.route
        self.visited = []
        self.exit_tick = 0
        self.update_initial_street()

    def __repr__(self):
        return f'<Route: {self.route}, Exit tick: {self.exit_tick}>'
