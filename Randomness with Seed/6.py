import numpy as np


np.random.seed(5)

for i in range(10):
  arr = np.random.randint(2, size = 1000)
  print(len(arr[arr == 1]) , len(arr[arr == 0]))