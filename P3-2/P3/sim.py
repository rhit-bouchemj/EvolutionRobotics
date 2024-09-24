import neuron
import numpy as np
import matplotlib.pyplot as plt

a = neuron.Perceptron()

X = np.linspace(-1.05,1.05,100)
Y = np.linspace(-1.05,1.05,100)
output = np.zeros((100,100))

i = 0
for x in X:
    j = 0
    for y in Y:
        output[i,j] = a.forward(x,y)
        j += 1
    i += 1

plt.pcolormesh(X,Y,output)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
