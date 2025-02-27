#Indexing and Slicing in Lists

import numpy as np


my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[-1])
print(my_list[2])
print(my_list[1:4])
print(my_list[:3])
print(my_list[3:])
print(my_list[::2])
print(my_list[::-1])

my_list[0] = 10
print(my_list)

del my_list[1]
print(my_list)

my_list[1:1] = [20, 30]
print(my_list)