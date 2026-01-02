import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
u = np.linspace(0, np.pi/2, 80)
3
v = np.linspace(0, 2*np.pi, 120)
u, v = np.meshgrid(u, v)
x = np.sin(u) * np.cos(v)
y = np.cos(u)
z = np.sin(u) * np.sin(v)
r = np.linspace(0, 1, 60)
t = np.linspace(0, 2*np.pi, 120)
r, t = np.meshgrid(r, t)
xd = r * np.cos(t)
yd = np.zeros_like(xd)
zd = r * np.sin(t)
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection=’3d’)
ax.plot_surface(x, y, z, linewidth=0, rstride=4, cstride=4,
antialiased=True, alpha=0.9)
ax.plot_surface(xd, yd, zd, linewidth=0, rstride=4, cstride=4,
antialiased=True, alpha=0.7)
ax.quiver(0, 0, 0, 0, -0.4, 0, length=1, linewidth=2)
sample_pt = np.array([0.7, np.sqrt(1-0.7**2), 0.0])
ax.quiver(sample_pt[0], sample_pt[1], sample_pt[2],
0.25*sample_pt[0], 0.25*sample_pt[1], 0.25*sample_pt[2],
length=1, linewidth=2)
ax.set_xlabel(’x’)
ax.set_ylabel(’y’)
ax.set_zlabel(’z’)
ax.set_title(’Hemisphere (y 0) and Disk (y = 0) | outward normals shown’)
ax.set_box_aspect([1,1,1])
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)
ax.view_init(elev=20, azim=30)
plt.tight_layout()
plt.show()

'''
Let v = ⟨x3 cos z, 1−3x2ycos z−3yz2 sin x, z3 sin x⟩be the vector field of
a fluid. Compute the flux of v across the surface x2 + y2 + z2 = 1 where
y >0 and the surface is oriented away from the origin. Use the divergence
theorem.
'''
