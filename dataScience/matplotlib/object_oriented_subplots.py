import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)  # axes is a list!
# for axe in axes:
#     axe.plot(x,y)

axes[0].plot(x, y)
axes[0].set_title('First plot')

axes[1].plot(y, x)
axes[1].set_title('Second plot')

plt.tight_layout()
plt.show()
