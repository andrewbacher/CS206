import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
import pybullet_data
import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
import numpy
import math
import random

pi = math.pi

physicsClient = p.connect(p.GUI)# object physicsClient handles physics and draws results to a GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#simulate gravity

planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")#loads in a box to the environment

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)
#targetAngles = numpy.zeros(10000)

targetAngles = (numpy.sin(numpy.linspace(-pi, pi, num = 1000)))

numpy.save("data/targetAngles.npy",targetAngles)
#exit()

for i in range(1000):#loop 1000 times
    p.stepSimulation()# increase physics inside simulation a small amount
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Bleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Fleg")

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Bleg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=targetAngles[i],

        maxForce=30)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_Fleg", controlMode=p.POSITION_CONTROL, targetPosition=targetAngles[i], maxForce=30)

    t.sleep(1/60)# program waits for 1/60 seconds
p.disconnect()#quits simulation
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)#saves sensor values in a file
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)#saves sensor values in a file


