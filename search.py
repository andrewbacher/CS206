import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
from solution import SOLUTION

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()
# for i in range(5):
#     os.system("py generate.py")
#     os.system("py simulate.py")
