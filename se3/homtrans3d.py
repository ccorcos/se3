import numpy
from rot3d import *

def xyzrpy2T(*args):
    """roll, pitch, yaw, x, y, z to SE(3) homogenous transform"""
    x,y,z,r,p,yaw = (0,0,0,0,0,0)
    if len(args) == 2:
        x,y,z = args[0]
        r,p,yaw = args[1]
    elif len(args) == 4:
        if (type(args[0]) == type(list())) or type(args[0]) == type(numpy.array([])):
            x,y,z = args[0]
            r,p,yaw = args[1:4]
        elif (type(args[3]) == type(list())) or type(args[3]) == type(numpy.array([])):
            x,y,z = args[0:3]
            r,p,yaw = args[3]
        else:
            raise
    elif len(args) == 6:
        x,y,z = args[0:3]
        r,p,yaw = args[3:6]
    else:
        raise
    R = rpy2R(r,p,yaw)
    T = numpy.eye(4)
    T[0:3, 0:3] = R
    T[0:3, 3] = [x,y,z]
    return T

def T2xyzrpy(T):
    r, p, yaw = R2rpy(T[0:3, 0:3])
    x, y, z = T[0:3, 3]
    return numpy.array([x, y, z, r, p, yaw])
