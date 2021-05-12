import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, id):
        self.solution = {}
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) *numpy.random.rand()
        self.weights * 2 - 1
        self.myID = id
        self.test = "A"
        #print(self.test)

    def Start_Simulation(self,directOrGUI,test):
        self.test = test
        self.Create_World()
        self.Create_Body(test)
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
        if(self.test =="A"):
            pyrosim.Send_Cube(name="Box", pos=[0, 0, 1.5], size=[25, 4.5, 3])
        else:
            pyrosim.Send_Cube(name="Box", pos=[0, 0, 1.5], size=[25, 5.5, 3])
        pyrosim.End()  # close sdf file

    def Create_Body(self,test):
        pyrosim.Start_URDF("body.urdf")  # Unified Robot Description Format file stores description of robot body
        self.test = test
        if (self.test == "A"):
            print("AAAA")
            pyrosim.Send_Cube(name="Torso", pos=[0, 0, 4],size=[1, 1, 1])  # stores the cube "Torso" at specified location
        if (self.test == "B"):
            pyrosim.Send_Cube(name="Torso", pos=[0, 0, 4.5], size=[1, 1, 1])  # stores the cube "Torso" at specified location

        if (self.test == "A"):
            pyrosim.Send_Joint(name="Torso_Bleg", parent="Torso", child="Bleg", type="revolute", position="0 -0.5 4",jointAxis="1 0 0")
        if (self.test == "B"):
            pyrosim.Send_Joint(name="Torso_Bleg", parent="Torso", child="Bleg", type="revolute", position="0 -0.5 4.5",jointAxis="1 0 0")

        pyrosim.Send_Cube(name="Bleg", pos=[0, -0.5, 0],size=[0.2, 1, 0.2])  # stores the cube "Bleg" at specified location

        if (self.test == "A"):
            pyrosim.Send_Joint(name="Torso_Fleg", parent="Torso", child="Fleg", type="revolute", position="0 0.5 4", jointAxis="-1 0 0")
        if (self.test == "B"):
            pyrosim.Send_Joint(name="Torso_Fleg", parent="Torso", child="Fleg", type="revolute", position="0 0.5 4.5",jointAxis="-1 0 0")

        pyrosim.Send_Cube(name="Fleg", pos=[0, 0.5, 0],size=[0.2, 1, 0.2])  # stores the cube "Fleg" at specified location

        if (self.test == "A"):
            pyrosim.Send_Joint(name="Torso_Lleg", parent="Torso", child="Lleg", type="revolute", position="-0.5 0 4",jointAxis="0 -1 0")

        if (self.test == "B"):
            pyrosim.Send_Joint(name="Torso_Lleg", parent="Torso", child="Lleg", type="revolute", position="-0.5 0 4.5",jointAxis="0 -1 0")

        pyrosim.Send_Cube(name="Lleg", pos=[-0.5, 0, 0],size=[1.0, 0.2, 0.2])

        if (self.test == "A"):
            pyrosim.Send_Joint(name="Torso_Rleg", parent="Torso", child="Rleg", type="revolute", position="0.5 0 4",jointAxis="0 1 0")
        if (self.test == "B"):
            pyrosim.Send_Joint(name="Torso_Rleg", parent="Torso", child="Rleg", type="revolute", position="0.5 0 4.5",jointAxis="0 1 0")

        pyrosim.Send_Cube(name="Rleg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Fleg_FrontLowerLeg", parent="Fleg", child="FrontLowerLeg", type="revolute", position="0 1 0",jointAxis="1 0 0")#
        if (self.test == "A"):
            pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        if (self.test == "B"):
            pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.75], size=[0.2, 0.2, 1.5])

        pyrosim.Send_Joint(name="Bleg_BackLowerLeg", parent="Bleg", child="BackLowerLeg", type="revolute",position="0 -1 0", jointAxis="1 0 0")
        if (self.test == "A"):
            pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        if (self.test == "B"):
            pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.75], size=[0.2, 0.2, 1.5])

        pyrosim.Send_Joint(name="Lleg_LeftLowerLeg", parent="Lleg", child="LeftLowerLeg", type="revolute",position="-1 0 0", jointAxis="0 -1 0")#
        if (self.test == "A"):
            pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        if (self.test == "B"):
            pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.75], size=[0.2, 0.2, 1.5])

        pyrosim.Send_Joint(name="Rleg_RightLowerLeg", parent="Rleg", child="RightLowerLeg", type="revolute",position="1 0 0", jointAxis="0 -1 0")
        if (self.test == "A"):
            pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        if(self.test == "B"):
            pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.75], size=[0.2, 0.2, 1.5])
        pyrosim.End()


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Bleg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Fleg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Lleg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="Rleg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        # pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")
        #
        # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Bleg")
        # pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_Fleg")
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_Lleg")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_Rleg")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Bleg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="Fleg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=10, jointName="Lleg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=11, jointName="Rleg_RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_Bleg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_Fleg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_Lleg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_Rleg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Bleg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Fleg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Lleg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Rleg_RightLowerLeg")

        # pyrosim.Send_Synapse(sourceNeuronName= 0, targetNeuronName= 3, weight= 1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=1.0)
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+9, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()






    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons-1)
        col = row = random.randint(0,c.numMotorNeurons-1)

        self.weights[row][col] = random.random() * 2 - 1

    def Set_ID(self,id):
        self.myID = id
