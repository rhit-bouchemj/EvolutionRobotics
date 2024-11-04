import ctrnn
import matplotlib.pyplot as plt
import numpy as np

size = 50
duration = 100
stepsize = 0.005

time = np.arange(0.0,duration,stepsize)

nn = ctrnn.CTRNN(size)

nn.load("ctrnn.npz")        #Load in network from saved params

nn.initializeState(np.zeros(size))

outputs = np.zeros((len(time),size))

# Run simulation
step = 0
for t in time:
    nn.step(stepsize)
    outputs[step] = nn.Outputs
    step += 1

# Plot activity
for i in range(size):
    plt.plot(time,outputs)
plt.xlabel("Time")
plt.ylabel("Output")
plt.title("Neural activity")
plt.show()
