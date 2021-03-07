import simulation
class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robot = simulation.p.loadURDF("body.urdf")
        simulation.pyrosim.Prepare_To_Simulate("body.urdf")