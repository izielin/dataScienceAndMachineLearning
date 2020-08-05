import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
array = np.array(my_data)
dictionary = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
print(pd.Series(my_data, labels))
print(pd.Series(array, labels))
print(pd.Series(dictionary))

print(pd.Series(labels))
print(pd.Series(data=[sum, print, len]))

series_1 = pd.Series([1, 2, 3, 4], ['USA', 'German Reich', 'USSR', 'Japan'])
series_2 = pd.Series([1, 5, 3, 4], ['USA', 'Italy', 'USSR', 'Japan'])
print(series_1)
print(series_2)

print(series_1['USA'])

print(series_1 + series_2)
