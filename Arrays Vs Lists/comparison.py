import numpy as np

lst = [1,3,2]
print(lst)
print(type(lst))
print('---')

arr = np.array([1,2,3])
print(arr)
print(type(arr))
print('---')

print(arr == lst)
print(arr.tolist() == lst)

print(sorted(arr) == sorted(lst))