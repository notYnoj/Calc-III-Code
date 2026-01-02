import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(X, Y):
return np.log(4*X + 3*Y)
x = np.linspace(-1.0, 3.0, 200)
y = np.linspace(-1.0, 3.0, 200)
X, Y = np.meshgrid(x, y)
Z = np.empty_like(X)
mask = (4*X + 3*Y) > 0
Z[mask] = f(X[mask], Y[mask])
Z[~mask] = np.nan # avoid bad log arg
3
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection=’3d’)
ax.plot_surface(X, Y, Z, rstride=3, cstride=3, linewidth=0.2, antialiased=True)
ax.set_xlabel(’x’)
ax.set_ylabel(’y’)
ax.set_zlabel(’f(x,y) = ln(4x+3y)’)
ax.set_title(’Surface: f(x,y) = ln(4x + 3y)’)
plt.tight_layout()
plt.savefig(’ln_surface.png’, dpi=300)
plt.show()
'''
A desired visualization of the surface z = f (x, y) =
ln(4x + 3y).
'''
