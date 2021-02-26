import street


class Intersection:

    def __init__(self, uid: int, schedule: list[str]):
        # Schedule stored in intersection as list of tuples containing a street id and how long
        # its on for
        self.schedule = schedule
        self.id = uid

        self.streets: list[street.Street] = []

    def step(self, tick: int) -> None:
        current_street = self.schedule[tick % len(self.schedule)]
        for street in self.streets:
            if street.name == current_street:
                street.light_green = True
                continue
            street.light_green = False

