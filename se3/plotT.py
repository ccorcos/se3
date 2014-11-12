import numpy
from rot3d import *
from homtrans3d import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def plotT(T, title=""):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect("equal")
    ax.set_title(title)

    # plot the transform
    pos = T[0:3,3]
    # column space of the rotation matrix is the rotated unit basis frame
    px = T[0:3,0]
    py = T[0:3,1]
    pz = T[0:3,2]
    # hack together equal aspect ratio and scaling the unit vectors to be visible
    points = numpy.array([pos,pos+px,pos+py,pos+pz, [0,0,0], [1,0,0], [0,1,0], [0,0,1]]).T
    X = points[0]
    Y = points[1]
    Z = points[2]
    max_range = numpy.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
    scale = max_range/2
    vx = numpy.array([pos,pos + px*scale]).T
    vy = numpy.array([pos,pos + py*scale]).T
    vz = numpy.array([pos,pos + pz*scale]).T
    x = Arrow3D(vx[0],vx[1],vx[2], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
    y = Arrow3D(vy[0],vy[1],vy[2], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
    z = Arrow3D(vz[0],vz[1],vz[2], mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
    ax.add_artist(x)
    ax.add_artist(y)
    ax.add_artist(z)

    # plot the basis
    i = Arrow3D([0,scale],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
    j = Arrow3D([0,0],[0,scale],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    k = Arrow3D([0,0],[0,0],[0,scale], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    ax.add_artist(i)
    ax.add_artist(j)
    ax.add_artist(k)

    # hack together the bounding box for 3d equal aspect ratio
    # http://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    Xb = 0.5*max_range*numpy.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
    Yb = 0.5*max_range*numpy.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
    Zb = 0.5*max_range*numpy.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())
    # Comment or uncomment following both lines to test the fake bounding box:
    for xb, yb, zb in zip(Xb, Yb, Zb):
       ax.plot([xb], [yb], [zb], 'w', alpha=0)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    plt.show()
