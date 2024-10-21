import ea                  
import fnn2 as fnn          
import invpend
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

expname = sys.argv[1]
id = sys.argv[2]

# currentpath = os.getcwd()
# os.chdir(currentpath+'/'+expname)

# ANN Params
layers = [3,10,10,1] #uses same network as execution?

# Task Params
duration = 20
stepsize = 0.02    
noisestd = 0.01 

# Time
time = np.arange(0.0,duration,stepsize)

# Load genotype
bestind_genotype = np.load(expname+"/gen"+id+".npy")

def evaluate(genotype): # repeat of fitness function but saving theta
    nn = fnn.FNN(layers)
    nn.setParams(genotype)  #Use the specific genotype of best iteration
    body = invpend.InvPendulum()
    out_hist = np.zeros((len(time),1))
    in_hist = np.zeros((len(time),3))
    f_hist=np.zeros(len(time))
    body.theta = np.pi          #record the variables as the fitness is calculated (doesn't evolve)
    body.theta_dot = 0
    k=0
    for t in time:
        inp = body.state()
        out = nn.forward(inp)*2-1 + np.random.normal(0.0,noisestd)
        f = body.step(stepsize, out)
        # body.render()
        in_hist[k] = inp   #record what variables were
        out_hist[k] = body.last_u#out
        f_hist[k] = f       #record instantaneous fitness
        k += 1              #index
    return in_hist, f_hist, out_hist

in_hist1, f_hist1, out_hist1 = evaluate(bestind_genotype)

plt.plot(in_hist1)
plt.plot(f_hist1*50,'k',label="Output")
plt.plot(out_hist1)
plt.xlabel("Time")
plt.ylabel("Inputs & Outputs & Fitness")
plt.legend(["cos_theta","sin_theta","ang. vel", "instant fitness", "Torque"])
plt.title("Agent #"+id)
plt.show()
