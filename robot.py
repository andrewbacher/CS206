import simulation
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import numpy
class ROBOT:
    def __init__(self):
        self.robot = simulation.p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for LinkName in pyrosim.linkNamesToIndices:
            self.sensors[LinkName] = SENSOR(LinkName)
       # self.sensors["Torso"] = SENSOR("Torso")
       # self.sensors["Bleg"] = SENSOR("Bleg")
       # self.sensors["Fleg"] = SENSOR("Fleg")

    def Sense(self, t):

        for key, value in self.sensors.items():
            value.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for JointName in pyrosim.jointNamesToIndices:
            self.motors[JointName] = MOTOR(JointName)
        #self.motors["Torso_Bleg"] = MOTOR("Torso_Bleg")
        #self.motors["Torso_Fleg"] = MOTOR("Torso_Fleg")

    def Act(self, t):
        for key, value in self.motors.items():
            value.Set_Value(self.robot, t)

    def Save_Values(self):
        for key, value in self.motors.items():
            numpy.save("data/Angles.npy", value.Motor_Values)  # saves sensor values in a f
        for key, value in self.sensors.items():
            numpy.save("data/SensorValues.npy",value.values)#saves sensor values in a file
