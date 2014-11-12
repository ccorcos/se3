import numpy
from se3 import *
from plotT import *

moveUp = xyzrpy2T([0,0,3],[0,0,0])
plotT(moveUp, 'move up')
upAndTiltThenUp = numpy.dot(upAndTilt, moveUp)
plotT(upAndTiltThenUp, "move up and tilt, then move up")
