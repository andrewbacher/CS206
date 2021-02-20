import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
import pybullet_data
import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it



physicsClient = p.connect(p.GUI)# object physicsClient handles physics and draws results to a GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#simulate gravity

planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")#loads in a box to the environment
pyrosim.Prepare_To_Simulate("body.urdf")
for i in range(1000):#loop 1000 times
    p.stepSimulation()# increase physics inside simulation a small amount
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Bleg")
    t.sleep(0.01666666666)# program waits for 1/60 seconds
p.disconnect()#quits simulation
