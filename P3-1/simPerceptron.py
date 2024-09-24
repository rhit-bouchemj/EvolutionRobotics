import neuron
import numpy as np
import matplotlib.pyplot as plt

a = neuron.Perceptron(2,0.1)
a.viz(10,"Before training")

trials = 1000

error = np.zeros(trials)

data = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
label = np.array([0,1,1,1])

for t in range(trials):
    for d in range(len(data)):
        error[t] += a.train(data[d],label[d])

a.viz(100,"After training")

plt.plot(error)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()
