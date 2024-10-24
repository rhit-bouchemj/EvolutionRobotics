import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as ps
import numpy as np
import matplotlib.pyplot as plt
import time


physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
# p.loadSDF("box.sdf")
robotId = p.loadURDF("body.urdf")

duration = 10000

ps.Prepare_To_Simulate(robotId)

x = np.linspace(0, 10*np.pi, duration)
leftY = np.tan(x) * np.pi/4
rightY = np.tan(x+np.pi/2) * np.pi/4
print(range(len(rightY)))
for index in range(len(rightY)):
    rightY[index] = min(rightY[index], 1.5)
    rightY[index] = max(rightY[index], -1.5)
    # leftY[index] = min(leftY[index], 1.5)
    # leftY[index] = max(leftY[index], -1.5)
    # print(edge)
# print(range(rightY))

# time.sleep(5)

# for i in range(duration):
#     # ps.Set_Motor_For_Joint(bodyIndex = robotId,
#     #                        jointName = b'leftFoot_Torso',
#     #                        controlMode = p.POSITION_CONTROL,
#     #                        targetPosition = leftY[i],
#     #                        maxForce = 500)
#     ps.Set_Motor_For_Joint(bodyIndex = robotId,
#                            jointName = b'rightFoot_Torso',
#                            controlMode = p.POSITION_CONTROL,
#                            targetPosition = rightY[i],
#                            maxForce = 500)

#     p.stepSimulation()
    # time.sleep(1/500)

p.disconnect()

plt.plot(rightY)
plt.xlabel("time")
plt.ylabel("position")
plt.legend("Kicker position")
plt.show()
