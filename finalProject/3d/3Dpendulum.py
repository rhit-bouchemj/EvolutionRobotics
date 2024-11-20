import pybullet as p
import pybullet_data

# Connect to PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the SDF file created by Pyrosim
p.loadSDF("invertedPendulum.sdf")

# Set gravity
p.setGravity(0, 0, -9.8)

# Run simulation
while True:
    p.stepSimulation()

p.disconnect()