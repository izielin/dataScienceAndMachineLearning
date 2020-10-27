import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')
print(iris['species'].unique())

# grid = sns.PairGrid(iris)
# grid.map(plt.scatter)
# grid.map_diag(sns.distplot)
# grid.map_upper(plt.scatter)
# grid.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
grid = sns.FacetGrid(data=tips, col='time', row='smoker')
grid.map(plt.scatter, 'total_bill', 'tip')
plt.show()
