import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label = "Bleg",linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = "Fleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()