import numpy
import matplotlib.pyplot
import constants as c
fitnessA =  numpy.load('a.npy')
fitnessB = numpy.load('b.npy')
meanA = numpy.zeros(c.populationSize)
meanB = numpy.zeros(c.populationSize)

stdA = numpy.zeros(c.numberOfGenerations)
stdB = numpy.zeros(c.numberOfGenerations)
for x in range(0,c.populationSize):
    rowA = fitnessA[x,:]


    rowB = fitnessB[x,:]

    meanA[x] = numpy.mean(rowA)
    meanB[x] = numpy.mean(rowB)
for x in range(0,c.numberOfGenerations):
    colA = fitnessA[:,x]
    print(colA)
    stdA[x] = numpy.std(colA)
    colB = fitnessB[:, x]
    stdB[x] = numpy.std(colB)
    print(colB)

s = meanA+stdA
matplotlib.pyplot.plot(meanA,label="a", linewidth=5)
matplotlib.pyplot.plot(meanB,label="B", linewidth=1)
matplotlib.pyplot.plot(s,label="a", linewidth=5)
matplotlib.pyplot.plot(meanB+stdB,label="B", linewidth=1)
matplotlib.pyplot.plot(meanA-stdA,label="a", linewidth=5)
matplotlib.pyplot.plot(meanB-stdB,label="B", linewidth=1)
#firstRowB = fitnessB[0, :]

#print(firstRowA)

#matplotlib.pyplot.plot(firstRowA, label = "a",linewidth = 3)

#matplotlib.pyplot.plot(firstRowB, label = "B")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()