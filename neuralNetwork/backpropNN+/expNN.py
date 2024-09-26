import neuron
import numpy as np
import matplotlib.pyplot as plt

# Takes about 20 seconds to run
# If you are experimenting with it, decrease the values of reps and trials

reps = 10
trials = 10000

data = np.array([[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,1],[0,-1],[1,0]])
label = np.array([1,1,1,1,0,0,0,0])

neurons = [2,4,6]
sdata = np.zeros((len(neurons),trials))
i = 0 
for s in neurons:
    error = np.zeros((reps,trials))
    for r in range(reps):
        a = neuron.NeuralNet(s,1)
        for t in range(trials):
            for d in range(len(data)):
                error[r][t] += a.train(data[d],label[d])
    sdata[i] = np.mean(error,0)
    i += 1

plt.plot(sdata.T)
plt.xlabel("Trials")
plt.ylabel("Error")
plt.legend(["N=2","N=4","N=6"])
plt.show()