import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# sns.set_context('notebook')
# sns.set_style('ticks')
# sns.despine(top=True, bottom=True)

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='viridis')
plt.show()
