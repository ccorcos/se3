import numpy
from se3 import *

pi = numpy.pi

# Dealing with floats and matrix mulitplication, there are very small deviations that cause problems
# when trying to determine equality.
p = SE3(0, 0, 0, 0, -pi/2, 0)
p.translate([10,0,0])
p.rotate([-pi/2,0,0])
p.rotate([0,0,pi/2])
p.translate([0,10,0])
print 'Notice the very small values that are appoximately zero. This is problematic because 1e-32 != 0'
print repr(p)

eq = SE3(0,0,0,-pi/2,0,0)
print ''
print 'This is effectively the same coordinate frame.'
print repr(eq)

print ''
print 'Equality is computed after rounding to the 10th decimal place which tends to be a reasonable assumption when dealing with robotics.'
print ''
print 'Equals to 10th decimal?', p == eq
print ''
print 'We also provide an approximate equals function so you can choose your own rounding decimal place'
print ''
print 'approx equals to 2nd decimal?', p.approxEq(eq, 2)
print 'approx equals to 17th decimal?', p.approxEq(eq, 17)
