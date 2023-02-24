import os
import time
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(4):``
#     os.system("python3.9 generate.py")
#     os.system("python3.9 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
time.sleep(120)
os.system("rm *brain*.nndf")
os.system("rm *body*.nndf")

