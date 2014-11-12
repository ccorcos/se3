import numpy
from se3 import *

pi = numpy.pi

# Sometimes you want to rotate or translate a coordinate frame, not from the local
# from but from the global frame. For example, a robot moving through an environment
# changing its own coordinate frame with respect to the rest of the world. But a robot
# manipulating an object is changing the object's local frame with respect to it's
# "global" frame. This concept of "global" will need to be polished once the robot is
# actually moving things around.

p = SE3(0, 0, 10, 0, -pi/2, 0)
p.plot('initally moved up and tilted up')
p.gTranslate([0,1,0])
p.plot('globally translated 1 in y')
p.gRotate([0,-pi/2,0])
p.plot('globally tilted up')
p.translate([-10,-1,0])
p.plot('locally translated "back 10" and "left 1"')
p.rotate([0,pi,0])
p.plot('locally pitched back to origin')
