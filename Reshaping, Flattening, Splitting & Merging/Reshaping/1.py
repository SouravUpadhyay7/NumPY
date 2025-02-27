import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

print(arr.shape)
print('-'*10)

reshaped_arr = np.reshape(arr, (3,2))
print(reshaped_arr)

print(reshaped_arr.shape)
     