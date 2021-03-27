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

    def Run(self):

        for i in range(c.numSteps):#loop 1000 times

            p.stepSimulation()# increase physics inside simulation a small amount
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            #t.sleep(c.sleep)# program waits for 1/60 seconds

    def Get_Fitness(self):

        self.robot.Get_Fitness()

    def __del__(self):

#        self.robot.Save_Values()
        for key,value in self.robot.sensors.items():
            value.Save_Values()
        p.disconnect()