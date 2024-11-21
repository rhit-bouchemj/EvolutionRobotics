import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import time
import numpy as np

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

duration = 5000

ps.Prepare_To_Simulate(robotId)

x = np.linspace(0,10*np.pi, duration)
y = np.sin(x)* np.pi/2

for i in range(duration):
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName=b'Foot1_Torso', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y[i], 
                           maxForce=500)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName=b'Foot2_Torso', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y[i], 
                           maxForce=500)
    
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName=b'Foot3_Torso', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=-y[i], 
                           maxForce=500)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName=b'Foot4_Torso', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y[i], 
                           maxForce=500)
    p.stepSimulation()
    time.sleep(1/300)

p.disconnect