# import ctrnn
# import matplotlib.pyplot as plt
# import numpy as np

# size = 40
# duration = 100
# stepsize = 0.005

# time = np.arange(0.0,duration,stepsize)

# nn = ctrnn.CTRNN(size)

# nn.load("ctrnnFarthest.npz")        #Load in network from saved params

# nn.initializeState(np.zeros(size))

# outputs = np.zeros((len(time),size))

# # Run simulation
# step = 0
# for t in time:
#     nn.step(stepsize)
#     outputs[step] = nn.Outputs
#     step += 1

# # Plot activity
# for i in range(size):
#     plt.plot(time,outputs)
# plt.xlabel("Time")
# plt.ylabel("Output")
# plt.title("Neural activity")
# plt.show()


import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as ps
import numpy as np
import matplotlib.pyplot as plt
import time
import ctrnn


#load physics client
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

#Load bodies
planeId = p.loadURDF("plane.urdf")
flipperID = p.loadURDF("flipperBody.urdf")
ps.Prepare_To_Simulate(flipperID)

#Load neural network
size = 4
duration = 20
stepsize = 0.01

# Initialize NN
nn = ctrnn.CTRNN(size)
nn.load("ctrnnBigFar.npz")        #Load in network from saved params
nn.initializeState(np.zeros(size))


# nn.initializeState(np.zeros(size))

t = np.arange(0.0,duration,stepsize)
outputs = np.zeros((len(t),size))
states = np.zeros((len(t),size))
fitness = np.zeros((len(t)))

# fit = 0.0
# posFlipper = p.getBasePositionAndOrientation(flipperID)
# print(posFlipper)
# vary initial condition
time.sleep(10)
ts = 0
step = 0
while ts < duration:
    ts += stepsize

    ps.Set_Motor_For_Joint(bodyIndex = flipperID,
                        jointName = b'rightFoot_Torso',
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = nn.Outputs[0],
                        maxForce = 500)
    
    ps.Set_Motor_For_Joint(bodyIndex = flipperID,
                        jointName = b'leftFoot_Torso',
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = nn.Outputs[1],
                        maxForce = 500)
    
    ps.Set_Motor_For_Joint(bodyIndex = flipperID,
                        jointName = b'leftCrutch_Torso',
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = nn.Outputs[2],
                        maxForce = 500)
    
    ps.Set_Motor_For_Joint(bodyIndex = flipperID,
                        jointName = b'rightCrutch_Torso',
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = nn.Outputs[3],
                        maxForce = 500)
    pos, _ = p.getBasePositionAndOrientation(flipperID)
    p.stepSimulation()
    nn.step(stepsize)

    nn.Inputs = np.zeros(size)
    nn.Inputs[0] = pos[0]
    nn.Inputs[1] = pos[1]
    # if (ts == stepsize):
    #     print(nn.Inputs)
    #     print(np.dot(nn.Weights.T, nn.Outputs))
    states[step] = nn.States
    outputs[step] = nn.Outputs
    fitness[step] = (np.abs(pos[0] - 3) + np.abs(pos[1] - 3))
    step += 1
    time.sleep(1/500)
    

p.disconnect()

activity = np.sum(np.abs(np.diff(outputs,axis=0)))/(duration*size*stepsize)
print("Overall activity: ",activity)    #this is what we look at to see if a neuron is changing over time ("turned on"/active)
print("Max Distance:", np.max(fitness))
bestFit = fitness[-1]

# Plot activity
plt.plot(t,outputs)
plt.xlabel("Time")
plt.ylabel("Outputs")
plt.title("Neural output activity")
plt.show()

# Plot activity
plt.plot(t,states)
plt.xlabel("Time")
plt.ylabel("States")
plt.title("Neural state activity")
plt.show()

plt.plot(t,fitness)
plt.xlabel("Time")
plt.ylabel("distance from Origin")
plt.title("Fitness Graph")
plt.show()

# Save CTRNN parameters for later
# nn.save("ctrnn")