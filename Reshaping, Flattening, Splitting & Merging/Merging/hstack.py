import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,5,2,9])
arr3 = np.array([9,2,3,5])
arr4 = np.array([8,2,9,4])

concat_arr = np.hstack((arr1,arr2,arr3,arr4))

print(concat_arr)