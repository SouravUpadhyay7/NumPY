import numpy as np
import time

# Creating the data
my_list = list(range(10000000))
my_array = np.arange(10000000)

# Search time for list
start_time = time.time()
for _ in range(100):
  if 5000000 in my_list:
    pass
end_time = time.time()
print('List : ', end_time - start_time)


# Search time for Array
start_time = time.time()
for _ in range(100):
  if 5000000 in my_array:
    pass
end_time = time.time()
print('Array : ', end_time - start_time)