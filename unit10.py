import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
grid = 100
r_max = np.sqrt(7/2)
x = np.linspace(-r_max, r_max, grid)
y = np.linspace(-r_max, r_max, grid)
3
X, Y = np.meshgrid(x, y)
R2 = X**2 + Y**2
# Points outside are bad
mask = R2 <= 7/2
X_masked = np.where(mask, X, np.nan)
Y_masked = np.where(mask, Y, np.nan)
Z_lower = np.where(mask, R2, np.nan)
Z_upper = np.where(mask, 7 - R2, np.nan)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection=’3d’)
ax.plot_surface(X_masked, Y_masked, Z_lower, color=’blue’, alpha=0.5,
rstride=5, cstride=5)
ax.plot_surface(X_masked, Y_masked, Z_upper, color=’red’, alpha=0.5,
rstride=5, cstride=5)
theta = np.linspace(0, 2*np.pi, 200)
r_int = np.sqrt(7/2)
xi = r_int * np.cos(theta)
yi = r_int * np.sin(theta)
zi = xi**2 + yi**2
ax.plot(xi, yi, zi, color=’k’, linewidth=2)
ax.set_xlabel(’x’)
ax.set_ylabel(’y’)
ax.set_zlabel(’z’)
ax.set_title(’Solid bounded by z=x^2+y^2 and z=7-x^2-y^2’)
ax.set_box_aspect([1,1,0.7])
plt.show()

'''
Solid bounded by region: Find the volume of the solid bounded below by the circular paraboloid z=
x^2 + y^2 and above by the circular paraboloid z= 7−x^2−y^2
'''
