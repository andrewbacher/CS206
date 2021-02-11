import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
pyrosim.Start_SDF("boxes.sdf")#names the world box
#Three variables associated with object size
length = 1
width = 1
height = 1
#three variables for object position
x = 0
y = 0
z = 0.5
pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])# stores box at specified location
pyrosim.Send_Cube(name="Box2",pos=[1,y,1],size=[length,width,height])# stores box at specified location
pyrosim.End()#close sdf file