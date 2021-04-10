import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, id):
        self.solution = {}
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights * 2 - 1
        self.myID = id

    def Start_Simulation(self,directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        call = "start /B py simulate.py " + directOrGUI + " " + str(self.myID)
       # print(call)
        os.system(call)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        os.system("CACLS fitness" + str(self.myID) + ".txt /e /p SYSTEM:r")
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        #print(self.fitness)
        os.system("del fitness" + str(self.myID) + ".txt")

    def Evaluate(self, directOrGUI):
        pass
       # self.Create_World()
       # self.Create_Body()
       # self.Create_Brain()
       # call = "start /B py simulate.py " + directOrGUI + " " +str(self.myID)
       # print(call)
       #os.system(call)
       # fitnessFileName = "fitness"+str(self.myID)+".txt"
       # while not os.path.exists(fitnessFileName):

        #    time.sleep(0.01)
        #f = open("fitness"+str(self.myID)+".txt","r")
        #self.fitness = float(f.read())
        #print(self.fitness)

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")  # names the world box
        pyrosim.End()  # close sdf file

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")  # Unified Robot Description Format file stores description of robot body
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1],size=[1, 1, 1])  # stores the cube "Torso" at specified location
        pyrosim.Send_Joint(name="Torso_Bleg", parent="Torso", child="Bleg", type="revolute", position="1 0 1")
        pyrosim.Send_Cube(name="Bleg", pos=[-0.5, 0, -0.5],size=[1, 1, 1])  # stores the cube "Bleg" at specified location
        pyrosim.Send_Joint(name="Torso_Fleg", parent="Torso", child="Fleg", type="revolute", position="0 0.5 1")
        pyrosim.Send_Cube(name="Fleg", pos=[0, 0.5, 0],size=[0.2, 1, 0.2])  # stores the cube "Fleg" at specified location
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
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
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons-1)
        col = row = random.randint(0,c.numMotorNeurons-1)

        self.weights[row][col] = random.random() * 2 - 1

    def Set_ID(self,id):
        self.myID = id
