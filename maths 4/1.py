import numpy as np


A = np.array([[5,4],[1,2]])

eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvalues, eigenvectors
print(eigenvalues)
print(eigenvectors)