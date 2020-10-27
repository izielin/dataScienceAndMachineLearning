import numpy as np
import pandas as pd

dictionary = {
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
}

df = pd.DataFrame(dictionary)
print(df)
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df.fillna(value='Empty value'))
print(df['A'].fillna(value=df['A'].mean()))
