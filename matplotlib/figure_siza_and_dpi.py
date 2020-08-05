import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

figure = plt.figure(figsize=(8, 4))
ax = figure.add_axes([.1, .1, .8, .8])
ax.plot(x, x**2, label='x squared')
ax.plot(x, x**3, label='x cubed')

ax.legend(loc=0)

# figure, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 4))
# axes[0].plot(x, y)
# axes[1].plot(y, x)

plt.tight_layout()
plt.show()

# figure.savefig('../matplotlib/save/fig1.png', dpi=200)
