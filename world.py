import simulation

class WORLD:
    def __init__(self):
        self.objects = simulation.p.loadSDF("world.sdf")  # loads in a box to the environment
        self.planeId = simulation.p.loadURDF("plane.urdf")