import numpy
from se3 import *

pi = numpy.pi

upAndTilt = xyzrpy2T([0,0,1],[0,-pi/2,0])
plotT(upAndTilt, 'move up and tilt back')
