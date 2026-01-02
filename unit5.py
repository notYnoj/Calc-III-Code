import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    with np.errstate(divide='ignore', invalid='ignore'):
        z = 9 * x * y / (x**2 + y**2)
        z[np.isnan(z)] = 0
    return z
x = np.linspace(-0.5, 0.5, 400)
y = np.linspace(-0.5, 0.5, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.9)
ax1.set_title("3D Surface of f(x,y) near the origin")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("f(x,y)")
ax2 = fig.add_subplot(1, 2, 2)
cont = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(cont)
ax2.set_title("Contour of f(x,y) near the origin")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
plt.tight_layout()
plt.show()

'''
In order for us to better visualize why the limit does not exist, I will draw
the graph of
f (x, y) = 9xy/
(x^2 + y^2.)
Near the origin. We will then consider how it looks like. Here is the graph:
As we see, the function rises along some paths (like y= x) and falls along
others (like the x-axis or y-axis).
Therefore, from the graph, we can see that as (x, y) →(0, 0), the surface
approaches different heights along different paths. This may assist in making
it more intuitive why the multivariable limit does not exist.
'''
