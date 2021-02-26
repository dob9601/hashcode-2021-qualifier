from solutions.solution import Solution

from world import World


class RandomSolution(Solution):
    name = 'random'

    def __init__(self, world: World):
        super().__init__(world)
