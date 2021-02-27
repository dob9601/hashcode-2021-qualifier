from world import World
from solvers import RandomSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'b.txt'

world = World(filename)
