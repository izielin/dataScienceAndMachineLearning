import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# create dataset
dataset = np.random.randn(25)

# create another rugplot
sns.rugplot(dataset);

# set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min, x_max, 100)

# set up the bandwidth
bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** 2

# create an empty kernel list
kernel_list = []

# plot each basis function
for data_point in dataset:
    # create a kernel for each point and append to list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    # scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis, kernel, color='grey', alpha=.5)

plt.ylim(0, 1)

# plot the sum of the basis function
sum_of_kde = np.sum(kernel_list, axis=0)

# plot figure
fig = plt.plot(x_axis, sum_of_kde, color='indianred')

# add the initial rugplot
sns.rugplot(dataset, c='indianred')

# get rid of y-tick marks
plt.yticks([])

# set title
plt.suptitle("sum of the Basis Functions")

plt.show()
