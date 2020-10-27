import numpy as  np
import pandas as pd

data = {
    'Company': ['Google', 'Google', 'Netflix', 'Netflix', 'AlliExpress', 'AlliExpress'],
    'Person': ['Sam', 'Charlie', 'Vanessa', 'Amy', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 234, 350]
}

df = pd.DataFrame(data)
print(df)
# byCompany = df.groupby('Company')
# print(byCompany.mean())
# print(byCompany.std())
# print(byCompany.sum().loc['AlliExpress'])
print('\n')
print(df.groupby('Company').sum().loc['Netflix'])

print('\n')
print(df.groupby('Company').count())

print('\n')
print(df.groupby('Company').max())

print('\n')
print(df.groupby('Company').min())

print('\n')
print(df.groupby('Company').describe().transpose())

