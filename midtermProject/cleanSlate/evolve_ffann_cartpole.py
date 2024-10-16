import ea
import fnn
import cartpole
import numpy as np
import matplotlib.pyplot as plt
import sys

id = sys.argv[1]

# ANN Params
layers = [4,10,10,1]

# Task Params
duration = 200
stepsize = 0.02
noisestd = 0.01

# Time
time = np.arange(0.0,duration,stepsize)

# EA Params
popsize = 100
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

theta_range = np.linspace(-0.05, 0.05, num=trials_theta)        # angle of the pole
thetadot_range = np.linspace(-0.05, 0.05, num=trials_thetadot)  # angular velocity of pole (angle deriv)
x_range = np.linspace(-0.05, 0.05, num=trials_x)                # position of the cart 
xdot_range = np.linspace(-0.05, 0.05, num=trials_xdot)          # velocity of the cart (position deriv)

# Fitness function
def fitnessFunction(genotype):
    nn = fnn.FNN(layers)
    nn.setParams(genotype)
    body = cartpole.Cartpole()
    fit = 0.0
    # vary initial condition
    for theta in theta_range: # theta starts at -0.05? then at 0.5 (to train with different starting positions)
        for theta_dot in thetadot_range: # diff angular velocity starts
            for x in x_range: # diff cart position
                for x_dot in xdot_range: # diff cart velocity starts
                    #initialize all variables for hte system (cart and pole)
                    body.theta = theta  
                    body.theta_dot = theta_dot
                    body.x = x
                    body.x_dot = x_dot
                    # make sure getting proper number of steps 
                    f = stepsize
                    t = 0
                    while f >= stepsize and t < duration:   #Until t is longer than the duration of the sym. or the system goes out of bounds (f becomes 0 when OoB)    
                        inp = body.state()  #input array into NN
                        out = nn.forward(inp)*2 - 1 + np.random.normal(0.0,noisestd)    #average the output around 0 (-1 to 1) and add random noise
                        f = body.step(stepsize, out)    
                        fit += f
                        t += stepsize
    return fit/(duration*total_trials)

# Evolve and visualize fitness over generations
ga = ea.MGA(fitnessFunction, genesize, popsize, recombProb, mutatProb, tournaments)
ga.run()
np.save("evol"+id+".npy",ga.bestfit)

# Get best evolved network and show its activity
bestind_num = int(ga.bestind[-1])
print(bestind_num)
bestind_genotype = ga.pop[bestind_num]
np.save("gen"+id+".npy",bestind_genotype)


