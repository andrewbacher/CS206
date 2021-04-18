import simulation
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain"+str(solutionID)+".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for LinkName in pyrosim.linkNamesToIndices:
            self.sensors[LinkName] = SENSOR(LinkName)

    def Sense(self, t):

        for key, value in self.sensors.items():
            value.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for JointName in pyrosim.jointNamesToIndices:
            self.motors[JointName] = MOTOR(JointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = (self.nn.Get_Value_Of(neuronName))*c.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
             #   print(neuronName+ ' '+jointName+' ')
              #  print(desiredAngle)


    def Think(self):
        self.nn.Update()
       # self.nn.Print()

    def Get_Fitness(self, solutionID):
        #stateOfLinkZero = p.getLinkState(self.robot, 0)
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)

        #positionOfLinkZero = stateOfLinkZero[0]
        basePosition = basePositionAndOrientation[0]

        #print(positionOfLinkZero)
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        xPosition = basePosition[2]
       # print(xCoordinateOfLinkZero)


        #f = open("fitness"+str(solutionID)+".txt","w")

        f = open("tmp" + str(solutionID) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")
        #os.system("rename tmp"+str(solutionID)+".txt fitness"+str(solutionID)+".txt")
        exit()