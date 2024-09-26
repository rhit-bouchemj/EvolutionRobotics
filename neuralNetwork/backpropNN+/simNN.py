import neuron
import numpy as np
import matplotlib.pyplot as plt

reps = 1
trials = 10000

# A simple problem
data = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
label = np.array([1,0,0,1])

# A slightly more complex problem
# data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,1],[0,-1],[1,0]])
# label = np.array([1,1,1,1,0,0,0,0])

error = np.zeros(trials)
a = neuron.NeuralNet(5,1)
a.viz2(100,"Before training",data,label)
for t in range(trials):
    for d in range(len(data)):
        error[t] += a.train(data[d],label[d])
a.viz2(100,"After training",data,label)

plt.plot(error.T)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()
