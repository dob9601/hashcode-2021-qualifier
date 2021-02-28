from world import World
from solvers.random_solver import RandomSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'a.txt'

world = World(filename)
solver = RandomSolver(world)
solver.run()
