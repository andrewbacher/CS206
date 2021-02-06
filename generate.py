import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
pyrosim.Start_SDF("box.sdf")#names the world box
pyrosim.Send_Cube(name="Box",pos=[0,0,0.5],size=[1,1,1])# stores box at specified location
pyrosim.End()#close sdf file