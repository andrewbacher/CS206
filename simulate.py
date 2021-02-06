import pybullet as p #for creating the simulated environment
import time as t #t.sleep() function
physicsClient = p.connect(p.GUI)# object physicsClient handles physics and draws results to a GUI

p.loadSDF("box.sdf")#loads in a box to the environment

for i in range(1000):#loop 1000 times
    p.stepSimulation()# increase physics inside simulation a small amount
    t.sleep(0.01666666666)# program waits for 1/60 seconds
p.disconnect()#quits simulation
