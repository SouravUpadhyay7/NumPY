import numpy as np

lst = [1,3,2]
arr = np.array([1,2,3])

print(lst)
del lst[-2]
print(lst)
print('---')

print(arr)
arr = np.delete(arr,-2)
print(arr)