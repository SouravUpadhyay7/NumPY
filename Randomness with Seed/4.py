import numpy as np

np.random.seed(5)

print(np.random.rand())
print(np.random.rand(3))

print(np.random.randint(10))
print(np.random.randint(10, size=(3, 5)))