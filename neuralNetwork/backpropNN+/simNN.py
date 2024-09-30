import neuron
import numpy as np
import matplotlib.pyplot as plt

reps = 1
trials = 10000

# A simple problem
data = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
label = np.array([1,-1,1,0])

# A slightly more complex problem w/ middle pocket
# data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[0,0],[-1,0],[0,1],[0,-1],[1,0]])
# label = np.array([1,1,1,1,1,0,0,0,0])

# Harder problem with multiple layers
# data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[0,0],[-1,0],[0,1],[0,-1],[1,0], [-0.5, -0.5], [-0.5, 0.5], [0.5, -0.5], [0.5, 0.5]])
# label = np.array([1,1,1,1,1,0,0,0,0, 0,1,0,0])

# data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,1],[0,-1],[1,0]])
# label = np.array([0,0,0,0,1,1,1,1])

error = np.zeros(trials)
a = neuron.NeuralNet(20,1)
a.viz2(100,"Before training",data,label)
for t in range(trials):
    for d in range(len(data)):
        error[t] += a.train(data[d],label[d])
a.viz2(100,"After training",data,label)

plt.plot(error.T)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()
