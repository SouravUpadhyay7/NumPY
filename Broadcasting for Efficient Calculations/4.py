import numpy as np


a = np.array([1,2,3])
b = np.array([[1, 2, 3],[4,5,6]])

print(a)
print(b)
print('-'*10)

print(np.bitwise_and(a,b))

print(np.bitwise_or(a,b))

print(np.bitwise_xor(a,b))

print(np.bitwise_not(a,b))

print(np.right_shift(a,b))

print(np.left_shift(a,b))