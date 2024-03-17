import numpy as np

# 1-D Array
# np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# for i in np1:
# 	print(i)


'''
# 2-D Array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np2:
	# print rows  
	# print(i)

	for j in i: 
		print(j)
'''

# 3-D Array 
np3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

'''
for i in np3: 
	# print(i)
	for j in i: 
		# print(j)
		for k in j:
			print(k)
'''

# Use np.nditer() -> easier and shortcut way 
for i in np.nditer(np3):
	print(i)