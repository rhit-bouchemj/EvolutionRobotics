import pybullet as p
import time
import pybullet_data

dt = 1/240 # pybullet simulation step
q0 = 0.5   # starting position (radian)
physicsClient = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
boxId = p.loadURDF("pendulumThing.urdf", useFixedBase=True)

# get rid of all the default damping forces
# p.changeDynamics(boxId, 1, linearDamping=0, angularDamping=0)
# p.changeDynamics(boxId, 2, linearDamping=0, angularDamping=0)

# go to the starting position
for _ in range(10000):
    p.setJointMotorControl2(bodyIndex=boxId, jointIndex=1, targetVelocity=0, controlMode=p.VELOCITY_CONTROL, force=0)
    # p.setJointMotorControl2(bodyIndex=boxId, jointIndex=1, controlMode=p.TORQUE_CONTROL, force=10)
    if _ % 100 == 0:
            print(p.getLinkState(bodyUniqueId=boxId, linkIndex=2))#[14])
    p.stepSimulation()
    time.sleep(dt)

# turn off the motor for the free 
p.setJointMotorControl2(bodyIndex=boxId, jointIndex=1, targetVelocity=0, controlMode=p.VELOCITY_CONTROL, force=0)
while True:
    p.stepSimulation()
    time.sleep(dt)
p.disconnect()