import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
pyrosim.Start_SDF("box.sdf")#names the world box
#Three variables associated with object size
length = 1
width = 2
height = 3
pyrosim.Send_Cube(name="Box",pos=[0,0,0.5],size=[length,width,height])# stores box at specified location
pyrosim.End()#close sdf file