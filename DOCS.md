
## 3D Rotation Matrices

$R_x$ is known as roll, $R_y$ is pich, and $R_z$ is yaw.

$$R_x(\theta) = \begin{bmatrix}
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
\end{bmatrix}\\[6pt]$$

Given yaw, pitch, and roll angles, $\alpha$, $\beta$, and $\gamma$, we can combine them to get the roll-pitch-yaw rotation matrix:

$$R = R_z(\alpha) \, R_y(\beta) \, R_x(\gamma)$$

## 3D Homogenous Transforms

Homogenous transforms combine rotation $R$ with position $t$ like so:

$$t = \begin{bmatrix}
x\\ y\\ z
\end{bmatrix} \\[6pt]$$

$$T = \begin{bmatrix}
R & t\\
0_{1\times3} & 1 \\[3pt]
\end{bmatrix} \\[6pt]$$

Thus, when combining transformations with multiplication, we get a translation from the previous orientation followed by a rotation:

$$T_1 \, T_2 = \begin{bmatrix}
R_1\,R_2 & t_1 + R_1\,t_2\\
0_{1\times3} & 1 \\[3pt]
\end{bmatrix} \\[6pt]$$
