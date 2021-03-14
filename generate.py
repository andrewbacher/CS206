import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it

def Create_World():
    pyrosim.Start_SDF("world.sdf")  # names the world box
    # Three variables associated with object size
    length = 1
    width = 1
    height = 1
    # three variables for object position
    x = -3
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])  # stores box at specified location

    pyrosim.End()  # close sdf file

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")  # Unified Robot Description Format file stores description of robot body
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])  # stores the cube "Torso" at specified location
    pyrosim.Send_Joint(name="Torso_Bleg", parent="Torso", child="Bleg", type="revolute", position="1 0 1")
    pyrosim.Send_Cube(name="Bleg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])  # stores the cube "Bleg" at specified location
    pyrosim.Send_Joint(name="Torso_Fleg", parent="Torso", child="Fleg", type="revolute", position="2 0 1")
    pyrosim.Send_Cube(name="Fleg", pos=[0.5, 0, -0.5], size=[1, 1, 1])  # stores the cube "Fleg" at specified location
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="Bleg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="Fleg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName="Torso_Bleg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Fleg")
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()