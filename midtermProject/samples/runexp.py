import os
import sys

expname = sys.argv[1]
reps = int(sys.argv[2])

currentpath = os.getcwd()

os.mkdir(expname)
os.chdir(currentpath+"/"+expname)

for i in range(reps):
    os.system("time python ../evolve_ffann_cartpole.py "+str(i)+" &")