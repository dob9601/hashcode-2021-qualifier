from solvers.genetic_solver import GeneticSolver
from world import World
from solvers.random_solver import RandomSolver
from solvers.genetic_solver import GeneticSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'b.txt'

world = World(filename)
solver = GeneticSolver(world)
solver.run()
