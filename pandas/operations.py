import numpy as np
import pandas as pd

df = pd.DataFrame(
    {'col1': [1, 2, 3, 4],
     'col2': [444, 555, 777, 444],
     'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df.head(), '\n')
print(df['col2'].nunique(), '\n')
print(df['col2'].unique(), '\n')
print(df['col2'].value_counts(), '\n')
print(df[(df['col1'] > 2) & (df['col2'] == 444)], '\n')

# def times2(x):
#     return x * 2
# print(df['col1'].apply(times2), '\n')

print(df['col2'].apply(lambda x: x * 2), '\n')

print(df.drop('col1', axis=1), '\n')
print(df.columns, '\n')
print(df.index, '\n')
print(df.sort_values('col2'), '\n')
print(df.isnull(), '\n')

data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'one', 'two', 'two', 'two'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1, 3, 2, 5, 4, 1]
}

df = pd.DataFrame(data)
print(df, '\n')
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']), '\n')
