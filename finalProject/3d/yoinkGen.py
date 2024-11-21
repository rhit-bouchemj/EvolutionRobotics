import pyrosim.pyrosim as ps


def Create_Robot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Foot1", pos=[0,0,0.5], size=[0.5,0.2,1])
    ps.Send_Joint(name="Foot1_Torso", parent="Foot1", child="Torso", type="revolute", position=[0,0.4,1])
    ps.Send_Cube(name="Torso",pos=[.75,0,0.5],size=[2,1,1])
    ps.Send_Joint(name="Foot2_Torso", parent="Torso", child="Foot2", type="revolute", position=[0,.4,0])
    ps.Send_Cube(name="Foot2", pos=[0,0,-0.5], size=[0.5,0.2,1])
    ps.Send_Joint(name="Foot3_Torso", parent="Torso", child="Foot3", type="revolute", position=[1.5,0.4,0])
    ps.Send_Cube(name="Foot3", pos=[0,0,-0.3], size=[0.5,0.2,1])
    ps.Send_Joint(name="Foot4_Torso", parent="Torso", child="Foot4", type="revolute", position=[1.5,-0.4,0])
    ps.Send_Cube(name="Foot4", pos=[0,0,-0.3], size=[0.5,0.2,1])
    ps.End()

Create_Robot()