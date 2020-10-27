import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# Part 1
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])
print(type(df['W']))

print(df[['Y', 'Z']])

df['Q'] = df['W'] + df['Y']
print(df)
df.drop('Q', axis=1, inplace=True)
# df.drop('E', axis=0, inplace=True)
print(df.shape)
print(df)

print(df.loc['A'])
print(df.iloc[3])
print(df.loc['D', 'W'])
print(df.loc[['A', 'B'], ['W', 'Y']])

# Part 2
print(df[df > 0])
print(df['W'] > 0)
print(df[df['W'] > 0])
print(df[df['Z'] < 0])

print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['X', 'Y']])

print(df[(df['W'] > 0) & (df['Y'] > 1)])

# df.reset_index()
new_index = 'CA NY WY OR CO'.split()
df['States'] = new_index
print(df.set_index('States'))

# Part 3
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)
print(df.loc['G1'].loc[1])
df.index.names = ['Groups', 'Num']
print(df)
print(df.loc['G2'].loc[2]['B'])
print(df.xs(1,level='Num'))
