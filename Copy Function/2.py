
#Copy function with lists

import numpy as np


lst = [1,2,3,4,5]
print(lst)
lst1 = lst
print(lst1)
print('-'*10)

lst[0] = 5
print(lst)
print(lst1)
print('-'*10)

lst1[0] = 4
print(lst)
print(lst1)

print()
print('*'*20)
print()

lst = [1,2,3,4,5]
print(lst)
lst1 = lst.copy()
print(lst1)
print('-'*10)

lst[0] = 5
print(lst)
print(lst1)
print('-'*10)
lst[0] = 1

lst1[0] = 5
print(lst)
print(lst1)