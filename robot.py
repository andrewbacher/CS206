import simulation
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                print(neuronName+ ' '+jointName+' ')
                print(desiredAngle)


    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        f = open("fitness.txt","w")
        f.write(str(xCoordinateOfLinkZero))
        exit()