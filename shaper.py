import numpy as np


# Create 1-D Numpy Array and Get Shape 
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)


# Create 2-D Numpy Array and Get Shape (row/columns-elements)
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np2)
print(np2.shape)


# Reshape 1-D array to 2-D array 
np3 = np1.reshape(3,4)
print(np3)


# Reshape 1-D array to 3-D array
np4 = np1.reshape(2,3,2)
print(np4)
print(np4.shape)


# Flatten to 1-D 
np5 = np1.reshape(-1)
print(np5)
print(np5.shape)
