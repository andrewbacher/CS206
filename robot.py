import simulation
from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
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

    def Act(self):
        for key, value in self.motors.items():
            value.Set_Value(self.robot)