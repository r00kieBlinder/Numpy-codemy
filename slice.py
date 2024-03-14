import numpy as np

# Slicing Numpy arrays 
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# return 2, 3, 4, 5
print(np1[1:5])
# return 5, 6, 7, 8
print(np1[4:8])

# Return from something till the end of an array?
# 4-9
print(np1[3:])

# Return negative slices 
# 7, 8
print(np1[-3:-1])

# Steps 
print(np1[1:5])
print(np1[1:5:2])

# Steps on the entire array
print(np1[::2])
print(np1[::3])

# Slice a 2-D array 
np2 = np.array([
	[1, 2, 3, 4, 5],
	[6, 7, 8, 9, 10]])
# pull out a single item
print(np2[1, 2])

# slice a 2-D array
# return 2, 3
print(np2[0:1, 1:3])

# slice from both rows 
# will return ([2, 3], [7, 8])
print(np2[0:2, 1:3])

