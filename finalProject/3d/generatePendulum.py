import pyrosim.pyrosim as ps

l = 1   # length
w = 1   # weight
h = 1   # height

x = 0
y = 0
z = h/2 # want to generate the first box not inside the plane

def Create_World():
    ps.Start_SDF("box.sdf")
    for i in range(10):
        ps.Send_Cube(name="box", pos=[0,0,0], size=[l,w,h])
        z += h
        l = 0.9 * l
        w = 0.9 * w
        h = 0.9 * h
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Foot", pos=[x,y,z], size=[l,w,h]) # Parent
    ps.Send_Joint(name="Foot_Torso", parent="Foot", child="Torso", type="revolute", position=[l/2, 0, h]) #position = RELATIVE??? value
    ps.Send_Cube(name="Torso", pos=[l/2, 0, h/2], size=[l,w,h]) # Child <-- position is recorded relatively to the joint to the parent; position = relative o the joint connecting it to the parent
    ps.End()

def Create_pendulum():
    # ps.Start_SDF("invertedPendulum.sdf")
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(
        name="Base",
        pos=[0, 0, 1],  # Position of the base (e.g., 1 unit above ground)
        size=[0.2, 0.2, 0.2],  # Size of the base
    )
    ps.Send_Cube(
        name="Beam",
        pos=[0, 0, 1],  # Position of the beam
        size=[0.1, 0.1, 2.0],  # Size of the beam (e.g., 2 units long)
    )
    ps.Send_Joint(
        name="Base_Beam_Joint",
        parent="Base",
        child="Beam",
        type="revolute",  # Joint type
        position=[0, 0, 1],  # Joint location (e.g., edge of the base)
        # jointAxis="0 1 0",  # Rotation axis (e.g., around the Y-axis)
    )
    ps.End()


def Create_RobotMan():
    limbLength, limbWidth = 1/4
    limbHeight = 1/2
    torsoAll = 2
    ps.Start_URDF("fullRobit.urdf")
    ps.Send_Cube(name="Torso", pos=[0,0,torsoAll], size=[torsoAll,torsoAll/2,torsoAll])
    ps.Send_Cube(name="Left Knee", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Cube(name="Left Foot", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Cube(name="Right Knee", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Cube(name="Right Foot", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Cube(name="Left Arm", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Cube(name="Right Arm", pos=[], size=[limbLength,limbWidth,limbHeight])
    ps.Send_Joint(name="leftKnee_Torso", parent="Torso", child="leftKnee", type="revolute", position=[torsoAll/2]) # want point in center of cubes



# Create_KickingBot()
Create_pendulum()
# Create_Robot()
