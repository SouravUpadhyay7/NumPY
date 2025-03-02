import numpy as np


A = np.array([[1,2],[3,4]])
B= np.array([[5],[6]])
solution = np.linalg.solve(A,B)
solution
print(solution)