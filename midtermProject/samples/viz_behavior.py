import ea                  
import fnn                
import cartpole             
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

expname = sys.argv[1]
id = sys.argv[2]

currentpath = os.getcwd()
os.chdir(currentpath+'/'+expname)

# ANN Params
layers = [4,10,10,1]

# Task Params
duration = 20
stepsize = 0.02    
noisestd = 0.01 

# Time
time = np.arange(0.0,duration,stepsize)

# Load genotype
bestind_genotype = np.load("genotype"+id+".npy")

def evaluate(genotype): # repeat of fitness function but saving theta
    nn = fnn.FNN(layers)
    nn.setParams(genotype)
    body = cartpole.Cartpole()
    out_hist = np.zeros((len(time),4))
    f_hist=np.zeros(len(time))
    body.theta = 0              
    body.theta_dot = 0      
    body.x = 0               
    body.x_dot = 0           
    k=0
    for t in time:
        inp = body.state()
        out = nn.forward(inp)*2-1 + np.random.normal(0.0,noisestd)
        f = body.step(stepsize, out)
        out_hist[k] = inp
        f_hist[k] = f
        k += 1
    return out_hist, f_hist

out_hist1, f_hist1 = evaluate(bestind_genotype)

plt.plot(out_hist1)
plt.plot(f_hist1*50,'k',label="Output")
plt.xlabel("Time")
plt.ylabel("Several different things!")
plt.legend(["x","vel","theta","ang. vel"])
plt.title("Agent #"+id)
plt.show()

