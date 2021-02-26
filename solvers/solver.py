import abc

from world import World


class Solver(abc.ABC):
    def __init__(self, world: World):
        self.filename = world.filename
        self.world = world

    @abc.abstractmethod
    def run(self) -> None:
        ...


    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError
