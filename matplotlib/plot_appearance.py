import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

fix, ax = plt.subplots()
ax.plot(x, x + 1, color='red', linewidth=.25)
ax.plot(x, x + 2, color='red', linewidth=.5)
ax.plot(x, x + 3, color='red', linewidth=1)
ax.plot(x, x + 4, color='red', linewidth=2)

# line style option
ax.plot(x, x + 5, color='green', lw=3, linestyle='-')
ax.plot(x, x + 6, color='green', lw=3, ls='-.')
ax.plot(x, x + 7, color='green', lw=3, ls='--')
ax.plot(x, x + 8, color='green', lw=3, ls=':')

# custom dash
line, = ax.plot(x, x + 9, color='black', lw=1.50)
line.set_dashes([5, 10, 15, 10])  # format: line, length, space, length

# possible marker symbols & marker size and colors
ax.plot(x, x + 10, color='blue', lw=3, ls='-.', marker='3')
ax.plot(x, x + 11, color='blue', lw=3, ls='--', marker='+', markersize=2)
ax.plot(x, x + 12, color='blue', lw=3, ls='--', marker='s', markerfacecolor='yellow', markeredgewidth=3,
        markeredgecolor='green')
ax.plot(x, x + 13, color='blue', lw=3, ls=':', marker='1')
ax.plot(x, x + 14, color='blue', lw=3, ls='--', marker='.', markersize=8)
ax.plot(x, x + 15, color='blue', lw=3, ls='-', marker=',')
ax.plot(x, x + 16, color='blue', lw=3, ls='--', marker='2')
ax.plot(x, x + 17, color='blue', lw=3, ls='-', marker='*')
ax.plot(x, x + 18, color='blue', lw=3, ls='-', marker='o')

ax.set_xlim([0,3])

plt.tight_layout()
plt.show()
