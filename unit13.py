import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 50)
U, V = np.meshgrid(u, v)
# I have a lot of these I might as well just place em into this
parametrizations = [
("<(2+v)cos(u), (2+v)sin(u), u+v²>",
lambda u, v: ((2 + v) * np.cos(u), (2 + v) * np.sin(u), u + v**2)),
("<(2+v)cos(u), (2+v)sin(u), v²>",
lambda u, v: ((2 + v) * np.cos(u), (2 + v) * np.sin(u), v**2)),
("<vcos(u), vsin(u), u+v²>",
lambda u, v: (v * np.cos(u), v * np.sin(u), u + v**2)),
("<(2+v)cos(u), (2+v)sin(u), u>",
lambda u, v: ((2 + v) * np.cos(u), (2 + v) * np.sin(u), u)),
("<vcos(u), vsin(u), v²>",
lambda u, v: (v * np.cos(u), v * np.sin(u), v**2))
]
fig = plt.figure(figsize=(20, 12))
for idx, (title, param) in enumerate(parametrizations, 1):
ax = fig.add_subplot(2, 3, idx, projection=’3d’)
X, Y, Z = param(U, V)
surf = ax.plot_surface(X, Y, Z, cmap=’viridis’, alpha=0.9, edgecolor=’none’)
ax.set_xlabel(’X’)
ax.set_ylabel(’Y’)
ax.set_zlabel(’Z’)
ax.set_title(title, fontsize=10)
max_range = max(np.ptp(X), np.ptp(Y), np.ptp(Z)) / 2.0
mid_x = (np.max(X) + np.min(X)) * 0.5
mid_y = (np.max(Y) + np.min(Y)) * 0.5
mid_z = (np.max(Z) + np.min(Z)) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
3
plt.tight_layout()
plt.show()

'''
Visualizing different parametrizations of multivaribale functions (question is very long :()
'''
