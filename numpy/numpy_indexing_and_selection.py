import numpy as np

array = np.arange(0, 11)
print(array[8])
print(array[2:6])
array[0:5] = 100
print(array)
array = np.arange(0, 11)

slice_of_array = array[0:6]
slice_of_array[:]=99
print(slice_of_array)
print(array)

array_copy = array.copy()
array_copy[-1] = 100

print(array, array_copy)