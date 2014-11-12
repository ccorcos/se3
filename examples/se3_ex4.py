import numpy
from se3 import *

pi = numpy.pi

# you can manipulate the current SE3 frame with rotate and translate
p = SE3(0, 0, 0, 0, -pi/2, 0)
p.plot("flip up")
p.translate([10,0,0])
p.plot("move up")
p.rotate([-pi/2,0,0])
p.plot("spin around x")
p.rotate([0,0,pi/2])
p.plot("spin down around z")
p.translate([0,10,0])
p.plot("move down")
