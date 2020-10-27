import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

sns.distplot(tips['total_bill'], bins=40)

# sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')


# sns.pairplot(tips, hue='sex')
# sns.rugplot(tips['total_bill'])


plt.show()
