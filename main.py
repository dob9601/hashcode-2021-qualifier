from world import World
from solvers.active_street_solver import ActiveStreetSolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'f.txt'

world = World(filename)
solver = ActiveStreetSolver(world)
solver.run()
