Special Euclidian 3-space (SE3)
===============================

Special euclidian 3-space is the world in which we live, dealing with 3D
position and orientation (so technically more than 3 dimensions, but
thats why its *special*).

The ``SE3`` class allows us to do typical transformations easily with
multiplication of the classes, as well as visualize the coordinate frame
and information about it. At the heard of this class are 3D Homogenous
transforms. Here's how they work.

3D Rotation Matrices
--------------------

:math:`R_x` is known as roll, :math:`R_y` is pich, and :math:`R_z` is
yaw.

.. math::

   R_x(\theta) = \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos \theta &  -\sin \theta \\[3pt]
   0 & \sin \theta  &  \cos \theta \\[3pt]
   \end{bmatrix} \\[6pt]
   R_y(\theta) = \begin{bmatrix}
   \cos \theta & 0 & \sin \theta \\[3pt]
   0 & 1 & 0 \\[3pt]
   -\sin \theta & 0 & \cos \theta \\
   \end{bmatrix} \\[6pt]
   R_z(\theta) = \begin{bmatrix}
   \cos \theta &  -\sin \theta & 0 \\[3pt]
   \sin \theta & \cos \theta & 0\\[3pt]
   0 & 0 & 1\\
   \end{bmatrix}\\[6pt]

Given yaw, pitch, and roll angles, :math:`\alpha`, :math:`\beta`, and
:math:`\gamma`, we can combine them to get the roll-pitch-yaw rotation
matrix:

.. math:: R = R_z(\alpha) \, R_y(\beta) \, R_x(\gamma)

3D Homogenous Transforms
------------------------

Homogenous transforms combine rotation :math:`R` with position :math:`t`
like so:

.. math::

   t = \begin{bmatrix}
   x\\ y\\ z
   \end{bmatrix} \\[6pt]

.. math::

   T = \begin{bmatrix}
   R & t\\
   0_{1\times3} & 1 \\[3pt]
   \end{bmatrix} \\[6pt]

Thus, when combining transformations with multiplication, we get a
translation from the previous orientation followed by a rotation:

.. math::

   T_1 \, T_2 = \begin{bmatrix}
   R_1\,R_2 & t_1 + R_1\,t_2\\
   0_{1\times3} & 1 \\[3pt]
   \end{bmatrix} \\[6pt]


