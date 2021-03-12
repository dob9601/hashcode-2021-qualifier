# hashcode-2021-qualifier
Hashcode 2021 qualification round simulator and a variety of solvers.

Simulator is 100% accurate (tested against the hashcode simulator at the time of the event)

## Solvers
Included are a variety of solvers:
 - GeneticSolver: A genetic algorithm approach for solving hashcode. Utilises a Redis server to distribute the workload across multiple machines. `redis_worker.py` should be run to consume tasks from this server
 - ActiveStreetSolver: A simple solver that sets the traffic light timings to be even on all streets with cars traveling on them at some point
 - BusiestPrioritySolver: Same as the ActiveStreetSolver but weighted towards streets with more cars.

## Scores at the end of the extended round
A: 2002

B: 4,566,388

C: 1,298,723

D: 1,706,203

E: 1,366,761

