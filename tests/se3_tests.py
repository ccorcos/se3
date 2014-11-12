
from unittest import TestCase
import numpy
from se3 import *

pi = numpy.pi

class TestSe3(TestCase):
    def test_rotx(self):
        # x rotates y to z and z to -y
        self.assertTrue(all(numpy.round(numpy.dot(rotx(pi/2), numpy.array([.1,.2,.3])), 3) == [0.1, -0.3, 0.2]))
    def test_roty(self):
        # y rotates x to -z and z to x
        self.assertTrue(all(numpy.round(numpy.dot(roty(pi/2), numpy.array([.1,.2,.3])), 3) == [0.3, 0.2, -0.1]))
    def test_rotz(self):
        # z rotates x to y and y to -x
        self.assertTrue(all(numpy.round(numpy.dot(rotz(pi/2), numpy.array([.1,.2,.3])), 3) == [-0.2, 0.1, 0.3]))
    def test_rpy2R_x(self):
        # x rotates y to z and z to -y
        self.assertTrue(all(numpy.round(numpy.dot(rpy2R(pi/2,0,0), numpy.array([.1,.2,.3])), 3) == [0.1, -0.3, 0.2]))
    def test_rpy2R_y(self):
        # y rotates x to -z and z to x
        self.assertTrue(all(numpy.round(numpy.dot(rpy2R(0,pi/2,0), numpy.array([.1,.2,.3])), 3) == [0.3, 0.2, -0.1]))
    def test_rpy2R_z(self):
        # z rotates x to y and y to -x
        self.assertTrue(all(numpy.round(numpy.dot(rpy2R(0,0,pi/2), numpy.array([.1,.2,.3])), 3) == [-0.2, 0.1, 0.3]))
    def test_rpy2R_order(self):
        # rotation in roll-pitch-yaw order should flip the x direction
        self.assertTrue(all(numpy.round(numpy.dot(rpy2R(pi/2,pi/2,pi/2), numpy.array([.1,.2,.3])), 3) == [0.3, 0.2, -0.1]))
    def test_R2rpy_inverse(self):
        # the reverse
        self.assertTrue(all( numpy.round(R2rpy(rpy2R(.1, .2, .3)), 3) == [0.1, 0.2, 0.3]))
    def test_R2rpy_atan2(self):
        # make sure we have the right sign (using arctan2)
        self.assertTrue(all(numpy.round(R2rpy(rpy2R(pi,0,0)),3) == numpy.round([pi,0,0],3)))
    def test_T2xyzrpy_xyzrpy2T(self):
        # the reverse
        self.assertTrue(all(numpy.round(T2xyzrpy(xyzrpy2T(1, 2, 3, .4, .5, .6)), 3) == [1, 2, 3, 0.4, 0.5, 0.6]))
