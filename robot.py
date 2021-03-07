import simulation
class ROBOT:
    def __init__(self):

        self.motors = {}
        self.robot = simulation.p.loadURDF("body.urdf")
        simulation.pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
    def Prepare_To_Sense(self):
        self.sensors = {}
        for LinkName in simulation.pyrosim.linkNamesToIndices:
            print(LinkName)