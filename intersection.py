import street


class Intersection:

    def __init__(self, uid: int):
        # Schedule stored in intersection as list of tuples containing a street id and how long
        # its on for
        self.schedule: list[str] = []
        self.id = uid

        self.streets: list[street.Street] = []

    def __repr__(self):
        return f'<Streets: {self.streets}>'
