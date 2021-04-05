from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #for x in range(0,(c.populationSize*c.numberOfGenerations)+2):
            #os.system("del brain"+str(x)+".nndf")

           # os.system("del fitness"+str(x)+".txt")

        os.system("del tmp*.txt")
        os.system("del brain*nndf")

        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(0,c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)

        #for x in range(0,c.populationSize):
         #   self.parents[x].Start_Simulation("DIRECT")

      #  for x in range(0, c.populationSize):
        #    self.parents[x].Wait_For_Simulation_To_End()

        for currentGeneration in range(c.numberOfGenerations):
             self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)


        self.print()

        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if(self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]

    def print(self):
        for key in self.parents:
            print(str(self.parents[key].fitness)+" "+str(self.children[key].fitness))
            print("")


    def Show_Best(self):
        best = 0
        for key in self.parents:
            if (self.parents[key].fitness < self.parents[best].fitness):
                best = key
        self.parents[best].Start_Simulation("GUI")




    def Evaluate(self,solutions):
        for x in range(0,c.populationSize):
            solutions[x].Start_Simulation("DIRECT")

        for x in range(0, c.populationSize):
            solutions[x].Wait_For_Simulation_To_End()
