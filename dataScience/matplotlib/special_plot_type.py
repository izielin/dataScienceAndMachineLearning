import numpy as np
import matplotlib.pyplot as plt
from random import sample

x = np.linspace(0, 5, 11)
y = x ** 2

plt.scatter(x, y)
plt.show()

data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

data_2 = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data_2, vert=True, patch_artist=True)
plt.show()
