##################################################################################
# Example script for evolving a feedforward neural network to solve XOR problem 
#
# Eduardo Izquierdo
# September 2024
##################################################################################

import numpy as np
import matplotlib.pyplot as plt
import fnn 
import ea

# Parameters of the XOR task
# dataset = [[-1,-1],[-1,1],[1,-1],[1,1]]
# labels = [0,1,1,0]


def fitnessFunction(genotype):
    # Step 1: Create the neural network.
    a = fnn.FNN(layers)

    # Step 2. Set the parameters of the neural network according to the genotype.
    a.setParams(genotype)
    
    # Step 3. For each training point in the dataset, evaluate the current neural network.
    error = 0.0
    for i in range(len(dataset)):
        error += np.abs(a.forward(dataset[i]) - labels[i])

    return 1 - (error/len(dataset))



# Function to visualize the best solution
def viz(neuralnet, dataset, label):
    X = np.linspace(-1.05, 1.05, 100)
    Y = np.linspace(-1.05, 1.05, 100)
    output = np.zeros((100,100))
    i = 0
    for x in X: 
        j = 0
        for y in Y: 
            output[i,j] = neuralnet.forward([x,y])
            j += 1
        i += 1
    plt.contourf(X,Y,output)
    plt.colorbar()
    plt.xlabel("x")
    plt.ylabel("y")
    for i in range(len(dataset)):
        if label[i] == 1:
            plt.plot(dataset[i][0],dataset[i][1],'wo')
        else:
            plt.plot(dataset[i][0],dataset[i][1],'wx')
    plt.show()  




# Parameters for another task
dataset = [[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[1,0],[0,-1],[0,1],[-0.5,-0.5],[-0.5,0.5],[0.5,-0.5],[0.5,0.5]]
labels = [1,1,1,1,1,1,1,1,0,0,0,0]  

numIterations = 10
bestList = []
# Parameters of the neural network
for i in range(numIterations):
    numberOfLayers = 5#np.random.randint(2,10)
    layers = []
    layers.append(2)
    for currentLayer in range(numberOfLayers - 2):
        layers.append(np.random.randint(3,10))
    layers.append(1)
    # layers = [2,5,7,10,7,5,1]
    # layers = [2,3,6,8,1]

    print(layers)

    # Parameters of the evolutionary algorithm
    genesize = np.sum(np.multiply(layers[1:],layers[:-1])) + np.sum(layers[1:]) 
    print("Number of parameters:",genesize)
    popsize = 50
    recombProb = 0.5
    mutatProb = 0.01
    tournaments = 100*popsize 
    # Evolve
    ga = ea.MGA(fitnessFunction, genesize, popsize, recombProb, mutatProb, tournaments)
    ga.run()
    # bestList.append(ga.getBestFit())
    plt.plot(ga.getBestFit(), label=i)

    # Obtain best agent
    best = int(ga.bestind[-1])
    # print(best)
    a = fnn.FNN(layers)
    a.setParams(ga.pop[best])

plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.title("Evolution")
plt.legend()
plt.show()
    # Visualize data
# viz(a, dataset, labels)

