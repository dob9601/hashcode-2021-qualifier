import street2


class Intersection:

    def __init__(self, uid: int):
        # Schedule stored in intersection as list of tuples containing a street id and how long
        # its on for
        self.schedule: list[str] = []
        self.id = uid

        self.streets: list[street2.Street] = []

    def step(self, tick: int) -> None:
        if not len(self.schedule):
            return

        current_street = self.schedule[tick % len(self.schedule)]

        for street in self.streets:
            if street.name == current_street:
                street.green_light = True
                continue
            street.green_light = False

    def __repr__(self):
        return f'<Streets: {self.streets}>'
