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

    def Sense(self, t):

        for key, value in self.sensors.items():
            value.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for JointName in pyrosim.jointNamesToIndices:
            self.motors[JointName] = MOTOR(JointName)

    def Act(self, t):
        for key, value in self.motors.items():
            value.Set_Value(self.robot, t)

    def Save_Values(self):
        for key, value in self.motors.items():
            numpy.save("data/Angles.npy", value.Motor_Values)  # saves sensor values in a f
