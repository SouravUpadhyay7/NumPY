import numpy as np

dct = {1 : 'apple', 2 : 'banana', 3 : 'cherry'}
print(dct)
print(type(dct))
print('-'*10)

arr = np.array(dct)
print(arr)
print(type(arr))
print('-'*10)

arr_k = np.array(list(dct.keys()))
arr_v = np.array(list(dct.values()))
print(arr_k)
print(type(arr_k))
print(arr_v)
print(type(arr_v))