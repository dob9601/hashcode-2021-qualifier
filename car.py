import street

class Car:

    def __init__(self, route: list[street.Street], current_position: int):
        self.route = route
        self.current_position = current_position

    def step(self) -> None:
        self.current_position += 1

        if self.current_position >= len(self.route[0]):
            if self.current_street.light_green and self.current_street.front_car == self:
                self.route.pop(0)
                self.current_position = 0
            else:
                print('Stuck behind other car')


    @property
    def current_street(self) -> street.Street:
        return self.route[0]

    @property
    def route_complete(self) -> bool:
        return not len(self.route)

    def __repr__(self):
        return f'<Route: {self.route}, Time on road: {self.current_position}, Route complete: {self.route_complete}>'
