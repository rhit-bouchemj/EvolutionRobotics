import ea                  
import fnn                
import cartpole         
import invpend    
import numpy as np
import matplotlib.pyplot as plt
import sys 

id = sys.argv[1]

# ANN Params
layers = [3,10,10,1]

# Task Params
duration = 200000   # how many steps the sim takes
stepsize = 0.02     # how mucht time is between each step
noisestd = 0.01     # the amt of noise in the system

# Time
time = np.arange(0.0,duration,stepsize)     # the array for each time section

# EA Params
popsize = 100   # number of elements in population
genesize = np.sum(np.multiply(layers[1:],layers[:-1])) + np.sum(layers[1:]) 
recombProb = 0.5
mutatProb = 0.01
tournaments = 500*popsize

# Fitness initialization ranges
trials_theta = 2
trials_thetadot = 2
trials_x = 2
trials_xdot = 2
total_trials = trials_theta*trials_thetadot*trials_x*trials_xdot

theta_range = np.linspace(-0.05, 0.05, num=trials_theta)
thetadot_range = np.linspace(-0.05, 0.05, num=trials_thetadot)
x_range = np.linspace(-0.05, 0.05, num=trials_x)
xdot_range = np.linspace(-0.05, 0.05, num=trials_xdot)

# Fitness function
def fitnessFunction(genotype):
    nn = fnn.FNN(layers)
    nn.setParams(genotype)
    # body = cartpole.Cartpole()
    body = invpend.InvPendulum()
    fit = 0.0
    for theta in theta_range:
        for theta_dot in thetadot_range:
            for x in x_range:
                for x_dot in xdot_range:
                    body.theta = theta
                    body.theta_dot = theta_dot
                    # body.x = x
                    # body.x_dot = x_dot
                    f = stepsize
                    t = 0
                    while f >= stepsize and t < duration:                        
                        inp = body.state()
                        out = nn.forward(inp)*2 - 1 + np.random.normal(0.0,noisestd)
                        f = body.step(stepsize, out)
                        fit += f
                        t += stepsize
    return fit/(duration*total_trials)

# Evolve and visualize fitness over generations
ga = ea.MGA(fitnessFunction, genesize, popsize, recombProb, mutatProb, tournaments)
ga.run()
np.save("evol"+id+".npy",ga.bestfit)

ga.showFitness()

# Get best evolved network and show its activity
bestind_num = int(ga.bestind[-1])
print(bestind_num)
bestind_genotype = ga.pop[bestind_num]
np.save("gen"+id+".npy",bestind_genotype)

# def evaluate(genotype): # repeat of fitness function but saving theta
#     nn = fnn.FNN(layers)
#     nn.setParams(genotype)
#     body = cartpole.Cartpole()
#     out_hist = np.zeros((len(time),4))
#     f_hist=np.zeros(len(time))
#     body.theta = 0              
#     body.theta_dot = 0      
#     body.x = 0               
#     body.x_dot = 0           
#     k=0
#     for t in time:
#         inp = body.state()
#         out = nn.forward(inp)*2-1 + np.random.normal(0.0,noisestd)
#         f = body.step(stepsize, out)
#         out_hist[k] = inp
#         f_hist[k] = f
#         k += 1
#     return out_hist, f_hist

# out_hist1, f_hist1 = evaluate(bestind_genotype)

# plt.plot(out_hist1)
# plt.plot(f_hist1*50,'k',label="Output")
# plt.legend(["x","vel","theta","ang. vel"])
# plt.show()

