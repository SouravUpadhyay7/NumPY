import numpy as np


l = np.linspace(0,10,5)
print(l)

l = np.linspace(1,10,10)
print(l)

l = np.linspace(1,10,10, endpoint = False)
print(l)

l,s= np.linspace(1,5,10, retstep = True)
print(l)
print(s)