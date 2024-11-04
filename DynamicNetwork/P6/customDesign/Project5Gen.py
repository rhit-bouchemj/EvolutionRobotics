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

def Create_KickingBot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Torso", pos=[x,y,z+h], size=[l,w,h]) #Child of left Foot
    ps.Send_Cube(name="leftFoot", pos=[l/2,0,-h/4], size=[l,w,h/2]) # parent because want to start from ground up (that way I don't have to calculate torso first)
    ps.Send_Cube(name="rightFoot", pos=[-l/2 ,0,-h/2], size=[l,w,h]) #Child of torso
    ps.Send_Cube(name="leftCrutch", pos=[0,w/2,-h/4], size=[l,w,h/2])
    ps.Send_Cube(name="rightCrutch", pos=[0,-w/2,-h/4], size=[l,w,h/2])
    ps.Send_Joint(name="leftFoot_Torso", parent="Torso", child="leftFoot", type="continuous", position=[l/2, 0, h]) # want point in center of cubes
    ps.Send_Joint(name="rightFoot_Torso", parent="Torso", child="rightFoot", type="revolute", position=[-l/2, 0, h])
    ps.Send_Joint(name="leftCrutch_Torso", parent="Torso", child="leftCrutch", type="revolute", position=[0, w/2, h])
    ps.Send_Joint(name="rightCrutch_Torso", parent="Torso", child="rightCrutch", type="revolute", position=[0, -w/2, h])
    ps.End()

def Create_FlipperBot():
    offsetL = 3*l
    offsetW = 3*w
    ps.Start_URDF("flipperBody.urdf")
    ps.Send_Cube(name="Torso", pos=[x+offsetL,y++offsetW,z+h], size=[l,w,h]) #Child of left Foot
    ps.Send_Cube(name="leftFoot", pos=[l/2,0,-h/4], size=[l,w,h/2]) # parent because want to start from ground up (that way I don't have to calculate torso first)
    ps.Send_Cube(name="rightFoot", pos=[-l/2,0,-h/4], size=[l,w,h/2]) #Child of torso
    ps.Send_Cube(name="leftCrutch", pos=[0,w/2,-h/4], size=[l,w,h/2])
    ps.Send_Cube(name="rightCrutch", pos=[0,-w/2,-h/4], size=[l,w,h/2])
    ps.Send_Joint(name="leftFoot_Torso", parent="Torso", child="leftFoot", type="revolute", position=[l/2+offsetL, offsetW, h]) # want point in center of cubes
    ps.Send_Joint(name="rightFoot_Torso", parent="Torso", child="rightFoot", type="revolute", position=[-l/2+offsetL, offsetW, h])
    ps.Send_Joint(name="leftCrutch_Torso", parent="Torso", child="leftCrutch", type="revolute", position=[offsetL, w/2+offsetW, h])
    ps.Send_Joint(name="rightCrutch_Torso", parent="Torso", child="rightCrutch", type="revolute", position=[offsetL, -w/2+offsetW, h])
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
Create_FlipperBot()
