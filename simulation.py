from robot import ROBOT
from world import WORLD
import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
import pybullet_data
import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
import numpy
import constants as c
class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)  # object physicsClient handles physics and draws results to a GUI
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero,c.zero,-c.g)#simulate gravity

        self.world = WORLD()
        self.robot = ROBOT()