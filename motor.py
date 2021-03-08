import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import simulation
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.Prepare_to_Act()
    def Prepare_to_Act(self):
        self.Motor_Values = numpy.zeros(c.numSteps)
        if(self.jointName == "Torso_Bleg"):
            self.amplitude = c.backAmp
            self.frequency = c.backFreq
            self.offset = c.backOff
        else:
            self.amplitude = c.frontAmp
            self.frequency = c.frontFreq
            self.offset = c.frontOff
        for i in range(c.numSteps):
            self.Motor_Values[i] = -self.amplitude*numpy.sin(self.frequency/160 * (i + self.offset))

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName=self.jointName, controlMode=simulation.p.POSITION_CONTROL, targetPosition=self.Motor_Values[t], maxForce=c.maxForce)