import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

targetAngles = numpy.load('data/targetAngles.npy')

matplotlib.pyplot.plot(targetAngles, label = "angle",linewidth = 3)
#matplotlib.pyplot.plot(backLegSensorValues, label = "Bleg",linewidth = 3)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Fleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()