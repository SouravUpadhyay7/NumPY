import numpy as np

arr = np.array([[1,2,3,2],[4,5,6,2],[7,8,9,2],[7,8,9,2]])
print(arr)
print('-'*10)

for _ in np.vsplit(arr, 4):
  print(_)