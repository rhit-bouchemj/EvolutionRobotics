import neuron
import numpy as np
import matplotlib.pyplot as plt

a = neuron.Perceptron()

a.viz(10, "before training")

trials = 100

error = np.zeros(trials)

for t in range (trials):
    error[t] = a.train(0,0,0) + a.train(0,1,0) + a.train(0,0,1) + a.train(1,1,1)

a.viz(10,"After Training")

plt.plot(error)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()