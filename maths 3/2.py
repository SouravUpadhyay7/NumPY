import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,10]])
B = np.array([[10],[11],[12]])
solution = np.linalg.solve(A,B)
solution
print(solution)