from world import World
from solvers.genetic_solver import GeneticSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'a.txt'

world = World(filename)
solver = GeneticSolver(world)
solver.run()
