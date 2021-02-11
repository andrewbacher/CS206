import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
import pybullet_data


physicsClient = p.connect(p.GUI)# object physicsClient handles physics and draws results to a GUI
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)#simulate gravity

planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")#loads in a box to the environment

for i in range(1000):#loop 1000 times
    p.stepSimulation()# increase physics inside simulation a small amount
    t.sleep(0.01666666666)# program waits for 1/60 seconds
p.disconnect()#quits simulation
