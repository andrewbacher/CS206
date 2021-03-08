import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
#frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/SensorValues.npy')

#bTargetAngles = numpy.load('data/backAngles.npy')
#fTargetAngles = numpy.load('data/frontAngles.npy')

fTargetAngles = numpy.load('data/Angles.npy')


#matplotlib.pyplot.plot(bTargetAngles, label = "Bangle",linewidth = 3)
matplotlib.pyplot.plot(fTargetAngles, label = "angles",linewidth = 3)
#matplotlib.pyplot.plot(backLegSensorValues, label = "Bleg",linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = "sensor values")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()