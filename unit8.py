import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(X, Y):
return X + Y
x = np.linspace(5, 7, 200)
y = np.linspace(2, 5, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z_avg = np.full_like(X, 9.5)
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection=’3d’)
ax.plot_surface(X, Y, Z, rstride=3, cstride=3, linewidth=0.2, antialiased=True, alpha
ax.plot_surface(X, Y, Z_avg, color=’red’, alpha=0.5)
ax.set_xlabel(’x’)
ax.set_ylabel(’y’)
ax.set_zlabel(’f(x,y) = x + y’)
ax.set_title(’hw9’)
plt.tight_layout()
plt.savefig(’surface_xy.png’, dpi=300)
3
plt.show()

'''
a figure that showcases our original function, z =
f (x, y) = x + y, with an average plane of z = 9.5 showcased. As you will
be able to see the plane seems to cut the region in about half, which would
make this our average value. R
'''
