import pybullet as p
import pybullet_data
import time

# Initialize PyBullet
physics_client = p.connect(p.GUI)  # GUI mode
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Set path to PyBullet data
p.setGravity(0, 0, -9.8)  # Set gravity

# Create a fixed base (anchor point for the pendulum)
base = p.createMultiBody(
    baseMass=0,  # Fixed base (immovable)
    baseCollisionShapeIndex=p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.1, 0.1, 0.1]),
    basePosition=[0, 0, 1],  # Positioned in space at z = 1
)

# Create the pendulum rod
rod_length = 1.0
rod = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.05, 0.05, rod_length / 2])

pendulum = p.createMultiBody(
    baseMass=1.0,  # Mass of the pendulum
    baseCollisionShapeIndex=rod,
    baseVisualShapeIndex=p.createVisualShape(
        p.GEOM_BOX,
        halfExtents=[0.05, 0.05, rod_length / 2],
        rgbaColor=[1, 0, 0, 1],  # Red color
    ),
    basePosition=[0, 0, 1 - rod_length / 2],  # Position the center of the rod below the base
)

nJoints = p.getNumJoints(pendulum)
print("skibidi rizz", nJoints)


jointNameToId = {}
for i in range(nJoints):
  jointInfo = p.getJointInfo(pendulum, 1)
  jointNameToId[jointInfo[1].decode('UTF-8')] = jointInfo[0]
  print("skibidi rizz", jointInfo)

# Add a revolute joint to pin the pendulum to the base
# p.setup_revolute()
p.createConstraint(
    parentBodyUniqueId=base,
    parentLinkIndex=-1,  # Parent is the base (fixed)
    childBodyUniqueId=pendulum,
    childLinkIndex=4,  # Child is the pendulum rod
    jointType=p.JOINT_GEAR,
    jointAxis=[0, 1, 0],  # Revolute joint around the Y-axis
    parentFramePosition=[0, 0, 1],  # Position of the joint on the base
    childFramePosition=[0, 0, rod_length / 2],  # Position of the joint on the pendulum
)

# Run the simulation
for _ in range(10000):
    p.stepSimulation()
    time.sleep(1 / 240)  # Slow down the simulation to real-time speed

# Disconnect PyBullet
p.disconnect()
