import numpy as np


arr = np.logspace(0,10,5)
print(arr)

arr = np.logspace(0,10,5, endpoint = False)
print(arr)

arr = np.logspace(0,10,5, base = 2)
print(arr)