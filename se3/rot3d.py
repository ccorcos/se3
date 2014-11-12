import numpy

def rotx(rad):
    return numpy.array([[1,0,0],[0,numpy.cos(rad), -numpy.sin(rad)], [0, numpy.sin(rad), numpy.cos(rad)]])

def roty(rad):
    return numpy.array([[numpy.cos(rad),0,numpy.sin(rad)],[0,1,0], [-numpy.sin(rad), 0, numpy.cos(rad)]])

def rotz(rad):
    return numpy.array([[numpy.cos(rad),-numpy.sin(rad),0],[numpy.sin(rad),numpy.cos(rad), 0], [0, 0, 1]])

def rpy2R(*args):
    """roll, pitch, yaw to SE(3) rotation matrix"""
    r,p,y = (0,0,0)
    if len(args) == 3:
        r,p,y = args
    elif len(args) == 1:
        r,p,y = args[0]
    else:
        raise
    R = numpy.dot(rotz(y),numpy.dot(roty(p),rotx(r)))
    return R

def R2rpy(R):
    r = R2roll(R)
    p = R2pitch(R)
    y = R2yaw(R)
    return numpy.array([r, p, y])

def R2roll(R):
    r = numpy.arctan2(R[2,1],R[2,2])
    return r

def R2pitch(R):
    p = numpy.arctan2(-R[2,0],numpy.sqrt(R[2,1]**2 + R[2,2]**2))
    return p

def R2yaw(R):
    y = numpy.arctan2(R[1,0],R[0,0])
    return y
