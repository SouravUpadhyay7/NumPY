import numpy as np

lst = [1,3,2]
arr = np.array([1,2,3])

print(lst)
lst.append(4)
print(lst)
print('---')

print(arr)
arr = np.append(arr, 4)
print(arr)