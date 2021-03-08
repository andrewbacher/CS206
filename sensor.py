import simulation
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = simulation.numpy.zeros(simulation.c.numSteps)
