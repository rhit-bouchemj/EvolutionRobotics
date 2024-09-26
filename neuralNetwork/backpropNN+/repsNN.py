import neuron
import numpy as np
import matplotlib.pyplot as plt

reps = 10
trials = 10000

data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,1],[0,-1],[1,0]])
label = np.array([1,1,1,1,0,0,0,0])

error = np.zeros((reps,trials))
for r in range(reps):
    a = neuron.NeuralNet(5,1)
    for t in range(trials):
        for d in range(len(data)):
            error[r][t] += a.train(data[d],label[d])
plt.plot(error.T)
plt.plot(np.mean(error,0),'k')
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()