import simulation
import numpy
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = simulation.numpy.zeros(simulation.c.numSteps)
    def Get_Value(self, t):
        self.values[t] = simulation.pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if(t == simulation.c.numSteps-1):
            print(self.values)

    def Save_Values(self):
        numpy.save("data/SensorValues.npy", self.values)  # saves sensor values in a file