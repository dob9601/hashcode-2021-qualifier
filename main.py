import world, schedule
from solvers.genetic_solver import GeneticSolver


"""
# Score should be 710,011
w=world2.World('e.txt')
s=schedule.Schedule.from_file('e_bps_779288') # d_ass_1583635

# Score should be 2,002
# w=world2.World('a.txt')
# s=schedule.Schedule.from_file('a_gs_2010')

# Score should be 1320177, comes out to 1320031
w=world2.World('f.txt')
s=schedule.Schedule.from_file('f_bps_1411194')

# Score should be 4566888
w=world2.World('b.txt')
s=schedule.Schedule.from_file('b_bps_4566888')
print(w.simulate(s))

w=world2.World('e.txt')
solver = GeneticSolver(w)
solver.run_from_existing('e_bps_779288')

w=world2.World('d.txt')
solver = GeneticSolver(w)
solver.run_from_existing('d_ass_1583635')

w=world2.World('d.txt')
s=schedule.Schedule.from_file('d_ass_1583635')

w=world.World('d.txt')
solver = GeneticSolver(w)
solver.run_from_existing('d_gs_1609104')

"""
w=world.World('d.txt')
s=schedule.Schedule.from_file('d_gs_1609104')
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
print(w.simulate(s))
