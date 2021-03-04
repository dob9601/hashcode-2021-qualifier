import street


class Intersection:

    def __init__(self, uid: int):
        # Schedule stored in intersection as list of tuples containing a street id and how long
        # its on for
        self.schedule: list[str] = []
        self.id = uid

        self.streets: list[street.Street] = []

    def step(self, tick: int) -> None:
        if len(self.schedule):
            current_street = self.schedule[tick % len(self.schedule)]
        else:
            current_street = ''

        for street in self.streets:
            if street.name == current_street:
                street.light_green = True
                continue
            street.light_green = False

    def __repr__(self):
        return f'<Streets: {self.streets}>'
