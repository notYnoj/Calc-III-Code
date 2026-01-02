import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0, np.pi/2, 300)
r = 4 * np.sin(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
fig, ax = plt.subplots(subplot_kw={’aspect’:’equal’})
ax.plot(x, y, ’b’, label=’r = 4 sin()’)
ax.fill_between(x, 0, y, color=’lightblue’, alpha=0.4)
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_xlabel(’x’)
ax.set_ylabel(’y’)
ax.set_title(’Region D: 0 r 4sin, 0 /2’)
ax.legend()
plt.tight_layout()
plt.savefig(’polar_region.png’, dpi=300)

plt.show()

'''
For the question: double integral(2costheta r dr d theta) between 0 r < 4sintheta and 0 <= theta <= pi/2
'''
