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
    ps.Send_Joint(name="Foot_Torso", parent="Foot", child="Torso", type="revolute", position=[l/2, 0, h]) #position = absolute value
    ps.Send_Cube(name="Torso", pos=[l/2, 0, h/2], size=[l,w,h]) # Child <-- position is recorded relatively to the joint to the parent; position = relative o the joint connecting it to the parent
    ps.End()

Create_Robot()
