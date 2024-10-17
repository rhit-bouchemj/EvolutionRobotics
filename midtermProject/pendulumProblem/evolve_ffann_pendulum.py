import ea
import fnn2 as fnn
import invpend
import numpy as np
import matplotlib.pyplot as plt
import sys

id = sys.argv[1]

# ANN Params
layers = [3,10,10,1]

# Task Params
duration = 20
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
total_trials = trials_theta*trials_thetadot

theta_range = np.linspace(np.pi - np.pi/20, np.pi + np.pi/20, num=trials_theta)        # angle of the pendulum
thetadot_range = np.linspace(-0.25, 0.25, num=trials_thetadot)  # angular velocity of pendulum (angle deriv)

# Fitness function
def fitnessFunction(genotype):
    nn = fnn.FNN(layers)
    nn.setParams(genotype)
    body = invpend.InvPendulum()
    fit = 0.0
    # vary initial condition
    for theta in theta_range: # theta starts at -0.05? then at 0.5 (to train with different starting positions)
        for theta_dot in thetadot_range: # diff angular velocity starts
                    #initialize all variables for hte system (cart and pole)
            body.theta = theta  
            body.theta_dot = theta_dot
            # make sure getting proper number of steps 
            f = stepsize
            t = 0
            while t < duration:   #Until t is longer than the duration of the sym. or the system goes out of bounds (f becomes 0 when OoB)    
                inp = body.state()  #input array into NN
                # print("inputStates: ", inp)
                out = nn.forward(inp)*2 - 1 + np.random.normal(0.0,noisestd)    #average the output around 0 (-1 to 1) and add random noise
                f = body.step(stepsize, out)    #Out is a 2D array; return cosine of angle of pendulm where max 1 is at pi(and updates all paremeters as if time passed)
                fit += f    #fitness determined based off of how long the system lasts (won't work for pendulumn)
                t += stepsize   #update t <-- get closer to stopping sim
    return fit/(duration*total_trials) #fitness function <-- averages fitness,(-) for down angle, 0 for up angle [never gets positive?]

# Evolve and visualize fitness over generations
ga = ea.MGA(fitnessFunction, genesize, popsize, recombProb, mutatProb, tournaments)
ga.run()
np.save("evol"+id+".npy",ga.bestfit)    #Save the best fit line to a file

# Get best evolved network and show its activity
bestind_num = int(ga.bestind[-1])   #Returns the index of the genotype that had the maximum fitness last
print(bestind_num)
bestind_genotype = ga.pop[bestind_num]
np.save("gen"+id+".npy",bestind_genotype)   #saves the best genotype array to a file
