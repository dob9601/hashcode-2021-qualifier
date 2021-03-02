from solvers.genetic_solver import GeneticSolver
from world import World
from schedule import Schedule
from solvers.random_solver import RandomSolver
from solvers.busiest_priority_solver import BusiestPrioritySolver

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
print = pp.pprint

filename = 'e.txt'

world = World(filename)
s = Schedule.from_file('e_bps_779288')
print(world.simulate(s))
