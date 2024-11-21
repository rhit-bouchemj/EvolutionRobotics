import pybullet as p
import pybullet_data
import time

# Initialize PyBullet
physics_client = p.connect(p.GUI)  # GUI mode
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Set path to PyBullet data
p.setGravity(0, 0, -9.8)  # Set gravity

# Create the floor
floor = p.createMultiBody(
    baseMass=0,  # Static object
    baseCollisionShapeIndex=p.createCollisionShape(p.GEOM_PLANE),
    basePosition=[0, 0, 0],  # Positioned at z = 0
)

#Create a static ball (immovable)
ball_radius = 0.1  # Radius of the ball
ball = p.createMultiBody(
    baseMass=0,  # Static (immovable)
    baseCollisionShapeIndex=p.createCollisionShape(p.GEOM_SPHERE, radius=ball_radius),
    baseVisualShapeIndex=p.createVisualShape(p.GEOM_SPHERE, radius=ball_radius, rgbaColor=[1, 0, 0, 1]),  # Red ball
    basePosition=[0, 0, 1],  # Positioned 1 unit above the floor
)

# Create the static cylindrical rod
rod_length = 0.5  # Total length of the rod
rod_radius = 0.05  # Radius of the cylinder

rod = p.createMultiBody(
    baseMass=1,  # Static (immovable)
    baseCollisionShapeIndex=p.createCollisionShape(p.GEOM_CYLINDER, radius=rod_radius, height=rod_length),
    baseVisualShapeIndex=p.createVisualShape(p.GEOM_CYLINDER, radius=rod_radius, length=rod_length, rgbaColor=[0, 1, 0, 1]  # Green rod
),
    basePosition=[0, 0, 0.75],  # Positioned 1 unit above the floor
)

# Create a fixed joint to connect the rod and ball
p.createConstraint(
    parentBodyUniqueId=rod,
    parentLinkIndex=-1,
    childBodyUniqueId=ball,
    childLinkIndex=-1,
    jointType=p.JOINT_GEAR,
    jointAxis=[0, 1, 1],  # Fixed joint has no axis of rotation
    parentFramePosition=[0, 0, 0.25],  # End of the rod
    childFramePosition=[0, 0, 0],  # Center of the ball
)

# Run the simulation
for _ in range(10000):
    p.stepSimulation()
    time.sleep(1 / 240)  # Real-time simulation

# Disconnect PyBullet
p.disconnect
