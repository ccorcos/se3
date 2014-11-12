import numpy
from se3 import *
from plotT import *

pi = numpy.pi


# multiplication works with SE3 object just like the dot product
# multiplication returns a new SE3 object while .transform transforms the current object
t0 = SE3(1, 0, 0, 0, -pi/10, 0)
t0.plot("forward and flip up")
t1 = SE3(0,0,1,pi/3,0,0)
t1.plot("up and roll")
t3 = t0*t1
t3.plot("forward, flip up, up, roll")
t0.plot("still the same")
t0.transform(t1)
t0.plot("transformed")
