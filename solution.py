import numpy
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    def __init__(self):
        self.solution = {}
        self.weights = numpy.random.rand(3,2)
        self.weights * 2 - 1

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("py simulate.py")
        f = open("fitness.txt","r")
        self.fitness = float(f.read())

    def Create_World(self):
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

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")  # Unified Robot Description Format file stores description of robot body
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5],size=[1, 1, 1])  # stores the cube "Torso" at specified location
        pyrosim.Send_Joint(name="Torso_Bleg", parent="Torso", child="Bleg", type="revolute", position="1 0 1")
        pyrosim.Send_Cube(name="Bleg", pos=[-0.5, 0, -0.5],size=[1, 1, 1])  # stores the cube "Bleg" at specified location
        pyrosim.Send_Joint(name="Torso_Fleg", parent="Torso", child="Fleg", type="revolute", position="2 0 1")
        pyrosim.Send_Cube(name="Fleg", pos=[0.5, 0, -0.5],size=[1, 1, 1])  # stores the cube "Fleg" at specified location
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Bleg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Fleg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Bleg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Fleg")
        # pyrosim.Send_Synapse(sourceNeuronName= 0, targetNeuronName= 3, weight= 1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=1.0)
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

