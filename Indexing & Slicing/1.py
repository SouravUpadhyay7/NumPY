#Indexing and Slicing in Arrays


import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

print(my_array[0])
print(my_array[-1])
print(my_array[2])

print(my_array[1:4])
print(my_array[:3])
print(my_array[3:])
print(my_array[::2])
print(my_array[::-1])

my_array[0] = 10
print(my_array)

np.delete(my_array, 1)
print(my_array)

np.insert(my_array, 1, [20, 30])
print(my_array)