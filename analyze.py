import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

bTargetAngles = numpy.load('data/backAngles.npy')
fTargetAngles = numpy.load('data/frontAngles.npy')
matplotlib.pyplot.plot(bTargetAngles, label = "Bangle",linewidth = 3)
matplotlib.pyplot.plot(fTargetAngles, label = "Fangle",linewidth = 3)
#matplotlib.pyplot.plot(backLegSensorValues, label = "Bleg",linewidth = 3)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Fleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()