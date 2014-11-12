import numpy
from rot3d import *
from homtrans3d import *
from plotT import *

class SE3:
    def __init__(self, *args):
        """x, y, z, roll, pitch, yaw"""
        if len(args) == 0:
            self.T = numpy.eye(4)
        else:
            self.T = xyzrpy2T(*args)

    def __repr__(self):
        return "SE3 Homogenous Transform \n\
\tx:\t%s \n\
\ty:\t%s \n\
\tz:\t%s \n\
\troll:\t%s \n\
\tpitch:\t%s \n\
\tyaw:\t%s" % tuple(T2xyzrpy(self.T))

    def __str__(self):
        return "SE3(%s, %s, %s, %s, %s, %s)" % tuple(T2xyzrpy(self.T))

    def plot(self, title=""):
        plotT(self.T, title)

    def translate(self, *args):
        move = numpy.array([0,0,0])
        if len(args) == 1:
            move = numpy.array(args[0])
        elif len(args) == 3:
            move = numpy.array(args)
        else:
            raise
        self.T = numpy.dot(self.T, xyzrpy2T(move,0,0,0))
        return self

    def rotate(self, *args):
        rot = numpy.array([0,0,0])
        if len(args) == 1:
            rot = numpy.array(args[0])
        elif len(args) == 3:
            rot = numpy.array(args)
        else:
            raise
        self.T = numpy.dot(self.T, xyzrpy2T(0,0,0,rot))
        return self

    def transform(self, other):
        if not isinstance(other, self.__class__):
            raise
        self.T = numpy.dot(self.T, other.T)
        return self

    # global translation, rotation, transformation
    # use this when you want to transform this coordinate
    # frame based on the global reference frame
    def gTranslate(self, *args):
        move = numpy.array([0,0,0])
        if len(args) == 1:
            move = numpy.array(args[0])
        elif len(args) == 3:
            move = numpy.array(args)
        else:
            raise
        self.T = numpy.dot(xyzrpy2T(move,0,0,0),self.T)
        return self

    def gRotate(self, *args):
        rot = numpy.array([0,0,0])
        if len(args) == 1:
            rot = numpy.array(args[0])
        elif len(args) == 3:
            rot = numpy.array(args)
        else:
            raise
        self.T = numpy.dot(xyzrpy2T(0,0,0,rot),self.T)
        return self

    def gTransform(self, other):
        if not isinstance(other, self.__class__):
            raise
        self.T = numpy.dot(other.T,self.T)
        return self

    def x(self):
        return self.T[0,3]
    def y(self):
        return self.T[1,3]
    def z(self):
        return self.T[2,3]
    def roll(self):
        return R2roll(self.T)
    def pitch(self):
        return R2pitch(self.T)
    def yaw(self):
        return R2yaw(self.T)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            raise
        se3 = SE3()
        se3.T = numpy.dot(self.T,other.T)
        return se3

    def __rmul__(self, other):
        if not isinstance(other, self.__class__):
            raise
        se3 = SE3()
        se3.T = numpy.dot(other.T,self.T)
        return se3

    def approxEq(self, other, decimal=2):
        if not isinstance(other, self.__class__):
            raise
        return numpy.all(numpy.round(self.T, decimal) == numpy.round(other.T, decimal))

    def __eq__(self, other):
        return self.approxEq(other, decimal=10)

    def __ne__(self, other):
        return not self.__eq__(other)
