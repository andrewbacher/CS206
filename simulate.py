import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
import pybullet_data
import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
import numpy



physicsClient = p.connect(p.GUI)# object physicsClient handles physics and draws results to a GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#simulate gravity

planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")#loads in a box to the environment

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for i in range(100):#loop 1000 times
    p.stepSimulation()# increase physics inside simulation a small amount
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Bleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Fleg")

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Bleg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=0.0,

        maxForce=500)

    t.sleep(0.01666666666)# program waits for 1/60 seconds
p.disconnect()#quits simulation
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)#saves sensor values in a file
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)#saves sensor values in a file

