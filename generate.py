import pyrosim.pyrosim as pyrosim #we dont need to write pyrosim.pyrosim every time we want to use it
pyrosim.Start_SDF("boxes.sdf")#names the world box
#Three variables associated with object size
length = 1
width = 1
height = 1
#three variables for object position
x = 0
y = 0
z = 0.35
for k in range(4):
    y = y +1
    for j in range(4):
        x = x+1
        for i in range(9git ):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])  # stores box at specified location
            z = z*.9
            z = z+1
            length = length*.9
            width = width*.9
            height = height*.9
        height = 1
        length = 1
        width = 1
        z = .35
    x = 0
pyrosim.End()#close sdf file