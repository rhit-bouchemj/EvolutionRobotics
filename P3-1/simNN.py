import neuron
import numpy as np
import matplotlib.pyplot as plt

#a.viz2(100,"Before training (random)")

reps = 10
trials = 10000

# data = np.array([[-1,-1],[-1,1],[1,-1],[1,1]])
# label = np.array([1,0,0,1])

data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,1],[0,-1],[1,0]])
label = np.array([1,1,1,1,0,0,0,0])

# sdata = np.zeros(10)
# for s in range(10):
error = np.zeros((reps,trials))
for r in range(reps):
    a = neuron.NeuralNet(7,1)
    for t in range(trials):
        for d in range(len(data)):
            error[r][t] += a.train(data[d],label[d])
    if error[r][-1] < 0.02:
        # sdata[s] += 1
        a.viz2(100,"After training",data,label)
plt.plot(error.T)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.show()
# plt.plot(sdata)
# plt.show()