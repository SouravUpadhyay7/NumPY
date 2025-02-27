
#Copy function with arrays


import numpy as np

arr = np.array([1,2,3,4,5])

arr_ = arr.copy()

print(arr)
print(arr_)
print('-'*10)

arr[0] = 5
print(arr)
print(arr_)
arr[0] = 1
print('-'*10)

arr_[0] = 5
print(arr)
print(arr_)