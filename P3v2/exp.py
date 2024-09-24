import neuron
import numpy as np
import matplotlib.pyplot as plt


data = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
label = np.array([0,1,1,1])

trials = 1000
reps = 100

errorA = np.zeros((reps,trials))
for r in range(reps):
    a = neuron.Perceptron(2,0.1)
    for t in range(trials):
        for d in range(len(data)):
            errorA[r][t] += a.train(data[d],label[d])


errorB = np.zeros((reps,trials))
for r in range(reps):
    a = neuron.Perceptron(2,0.5)
    for t in range(trials):
        for d in range(len(data)):
            errorB[r][t] += a.train(data[d],label[d])

plt.plot(errorA.T)
plt.plot(errorB.T)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()
