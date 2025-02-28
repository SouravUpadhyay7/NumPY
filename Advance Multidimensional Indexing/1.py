



import numpy as np

arr = np.array([[[1,2,3],[4,5,6],[1,3,5]], [[7,8,9],[10,11,12],[4,5,3]], [[7,8,9],[10,11,12],[4,5,3]]])
print(arr)
print('-'*10)

# Access a specific Element
print(arr[0][1][2])
print(arr[0,1,2])
print('-'*10)

# Access a specific row
print(arr[0])
print(arr[0,:])
print(arr[0,:,:])
print(arr[:,0,:])
print(arr[:,:,0])
print('-'*10)

# Access with specific case
print(arr[[1,2], : , :])
print(arr[[1,2], : , 1])
print('-'*10)

# Access with specific conditions
print(arr[arr>5])
arr[arr >= 18] = "True"
print(arr)