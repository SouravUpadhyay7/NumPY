import numpy as np


arr = np.array([[1,2,3,2],[4,5,6,2],[7,8,9,2],[7,8,9,2]])
print(arr)

print('-'*10)

split_arr = np.split(arr, 2, axis = 1)
print(split_arr)