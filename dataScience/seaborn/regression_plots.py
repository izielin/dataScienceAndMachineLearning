import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'],
#            scatter_kws={'s': 100, })

sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time', hue='smoker', aspect=.6, height=9)

plt.show()
