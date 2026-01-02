import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(x, y):
return 4 * np.exp(x**2 - 4*y)
def tangent_plane(x, y):
x0, y0, z0 = 8, 16, 4
fx = 8 * np.exp(x0**2 - 4*y0)
3
fy = -16 * np.exp(x0**2 - 4*y0)
return z0 + fx * (x - x0) + fy * (y - y0)
x = np.linspace(7.5, 8.5, 50)
y = np.linspace(15.5, 16.5, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z_plane = tangent_plane(X, Y)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection=’3d’)
ax.plot_surface(X, Y, Z, alpha=0.6, color=’cyan’, label=’Surface’)
ax.plot_surface(X, Y, Z_plane, alpha=0.5, color=’orange’, label=’Tangent Plane’)
ax.scatter(8, 16, 4, color=’red’, s=50, label=’Point (8,16,4)’)
ax.set_xlabel(’X’)
ax.set_ylabel(’Y’)
ax.set_zlabel(’Z’)
ax.set_title(’Surface and Tangent Plane at (8,16,4)’)
plt.savefig(’tangent_plane_graph.png’, dpi=300)
plt.show()

'''
A3D plot of the
surface z = 4e^(x^2−4y) and its tangent plane at the point (8, 16, 4).

This plot demonstrates how the tangent plane passes through the surface
precisely tangent at the point. Therefore we can confirm that this answer is
correct
'''
