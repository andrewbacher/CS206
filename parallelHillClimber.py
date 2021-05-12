from solution import SOLUTION
import constants as c
import copy
import os
import numpy as numpy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #for x in range(0,(c.populationSize*c.numberOfGenerations)+2):
            #os.system("del brain"+str(x)+".nndf")

           # os.system("del fitness"+str(x)+".txt")

        os.system("del tmp*.txt")
        os.system("del brain*nndf")


        self.matrix = numpy.zeros((c.populationSize,c.numberOfGenerations))
        self.matrixB = numpy.zeros((c.populationSize, c.numberOfGenerations))
        self.currentGen = 0

        os.system("del fitness*.txt")
        self.parents = {}
        self.parentsB = {}
        self.nextAvailableID = 0
        for x in range(0,c.populationSize):

            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        for x in range(0, c.populationSize):
            self.parentsB[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents,"A")
        self.Evaluate(self.parentsB,"B")

        #for x in range(0,c.populationSize):
         #   self.parents[x].Start_Simulation("DIRECT")

      #  for x in range(0, c.populationSize):
        #    self.parents[x].Wait_For_Simulation_To_End()

        for currentGeneration in range(c.numberOfGenerations):
             self.currentGen = currentGeneration
             self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children,"A")
        self.Evaluate(self.childrenB,"B")

        self.print()

        self.Select()

    def Spawn(self):
        self.children = {}
        self.childrenB = {}

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            self.childrenB[key] = copy.deepcopy(self.parentsB[key])
            self.childrenB[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()
            self.childrenB[key].Mutate()

    def Select(self):
        for key in self.parents:
            if(self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]
            if (self.parentsB[key].fitness > self.childrenB[key].fitness):
                self.parentsB[key] = self.childrenB[key]
            self.matrix[(key,self.currentGen)] = self.parents[key].fitness
            self.matrixB[(key, self.currentGen)] = self.parentsB[key].fitness

    def print(self):
        for key in self.parents:
            print(str(self.parents[key].fitness)+" "+str(self.children[key].fitness))
            print("")
            print("B test "+str(self.parentsB[key].fitness) + " " + str(self.childrenB[key].fitness))
            print("")




    def Show_Best(self):
        best = 0
        bestB = 0
        for key in self.parents:
            if (self.parents[key].fitness < self.parents[best].fitness):
                best = key
        for key in self.parentsB:
            if (self.parentsB[key].fitness < self.parentsB[bestB].fitness):
                bestB = key
        print(self.matrix)
        print(self.matrixB)
        numpy.savetxt('test.txt', self.matrix)
        numpy.savetxt('testB.txt', self.matrixB)
        print("Best Fitness A: "+str(self.parents[best].fitness))
        print("Best Fitness B: " + str(self.parentsB[bestB].fitness))
        #self.parentsB[bestB].Start_Simulation("GUI","B")
        self.parents[best].Start_Simulation("GUI","A")
        self.parents[best].Wait_For_Simulation_To_End()
        self.parentsB[bestB].Start_Simulation("GUI","B")
        #self.parentsB[bestB].Start_Simulation("GUI", "B")




    def Evaluate(self,solutions,test):
        for x in range(0,c.populationSize):
            solutions[x].Start_Simulation("DIRECT",test)

        for x in range(0, c.populationSize):
            solutions[x].Wait_For_Simulation_To_End()
