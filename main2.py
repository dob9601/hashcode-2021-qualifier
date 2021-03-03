from solvers.genetic_solver import GeneticSolver
from world2 import World
from solvers.random_solver import RandomSolver
from solvers.genetic_solver import GeneticSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'e.txt'

world = World(filename)
solver = GeneticSolver(world)
solver.run_from_existing('e_bps_779288')
