import pandas as pd

df1 = pd.DataFrame(
    {'A': ['A0', 'A1', 'A2', 'A3'],
     'B': ['B0', 'B1', 'B2', 'B3'],
     'C': ['C0', 'C1', 'C2', 'C3'],
     'D': ['D0', 'D1', 'D2', 'D3']},
    index=[0, 1, 2, 3])

df2 = pd.DataFrame(
    {'A': ['A4', 'A5', 'A6', 'A7'],
     'B': ['B4', 'B5', 'B6', 'B7'],
     'C': ['C4', 'C5', 'C6', 'C7'],
     'D': ['D4', 'D5', 'D6', 'D7']},
    index=[4, 5, 6, 7])

df3 = pd.DataFrame(
    {'A': ['A8', 'A9', 'A10', 'A11'],
     'B': ['B8', 'B9', 'B10', 'B11'],
     'C': ['C8', 'C9', 'C10', 'C11'],
     'D': ['D8', 'D9', 'D10', 'D11']},
    index=[8, 9, 10, 11])

print(df1, '\n')
print(df2, '\n')
print(df3, '\n')

# Concatenation - glues together DataFrames - dimensions should mach along the axis which are concatenating on.
print(pd.concat([df1, df2, df3]), '\n')

#############################################

left = pd.DataFrame({
    'key': ['k0', 'k1', 'k2', 'k3'],
    'a': ['a0', 'a1', 'a2', 'a3'],
    'b': ['b0', 'b1', 'b2', 'b3']})

right = pd.DataFrame({
    'key': ['k0', 'k1', 'k2', 'k3'],
    'c': ['c0', 'c1', 'c2', 'c3'],
    'd': ['d0', 'd1', 'd2', 'd3']})

print(left, '\n')
print(right, '\n')

# Merging - allows to merge DataFrames together
print(pd.merge(left, right, how='inner', on='key'), '\n')

left = pd.DataFrame({
    'key1': ['k0', 'k0', 'k1', 'k2'],
    'key2': ['k0', 'k1', 'k0', 'k1'],
    'a': ['a0', 'a1', 'a2', 'a3'],
    'b': ['b0', 'b1', 'b2', 'b3']})

right = pd.DataFrame({
    'key1': ['k0', 'k1', 'k1', 'k2'],
    'key2': ['k0', 'k0', 'k0', 'k0'],
    'c': ['c0', 'c1', 'c2', 'c3'],
    'd': ['d0', 'd1', 'd2', 'd3']})

print(pd.merge(left, right, on=['key1', 'key2']), '\n')

#############################################

left = pd.DataFrame({
    'a': ['a0', 'a1', 'a2'],
    'b': ['b0', 'b1', 'b2']},
    index=['k0', 'k1', 'k2'])

right = pd.DataFrame({
    'c': ['c0', 'c2', 'c3'],
    'd': ['d0', 'd2', 'd3']},
    index=['k0', 'k2', 'k3'])

# joining - method for combining the columns of two potentially differently-indexed DataFrames into a single result
print(left.join(right), '\n')