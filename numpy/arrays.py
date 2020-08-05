import numpy as np

my_list = [1, 2, 3]
first_arr = np.array(my_list)
print(first_arr)

my_matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
second_arr = np.array(my_matrix)
print(second_arr)

print(np.arange(0, 11, 2))

print(np.zeros(3))

print(np.ones((3, 2)))

print(np.linspace(0, 5, 10))

print(np.eye(4))

# random numbers

print(np.random.rand(5))
print(np.random.rand(5, 5))
print(np.random.randn(2, 3))
print(np.random.randint(2, 10, 5))

arr = np.arange(25)
rand_arr = np.random.randint(0, 20, 10)
print(arr, rand_arr)

arr = arr.reshape(5, 5)
print(arr)

print(arr.max())
print(arr.min())
print(arr.argmax())
print(arr.argmin())

print(arr.shape)