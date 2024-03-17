import numpy as np

# np.sort()
np1 = np.array([9,4,7,2,1,5,0,3])
print(np1)
print(np.sort(np1))


# Alphabetical
np2 = np.array(["Fahim", "Zarif", "Raka", "Ahbab", "Arbab"])
print(np2)
print(np.sort(np2))

# Booleans T/F
np3 = np.array([True, False, False, True])
print(np3)
print(np.sort(np3))


# Returns a copy and does not change the original 
print(np1)
print(np.sort(np1))
print(np1) # original does not change even if we use np.sort() func


# 2-D array sort
np4 = np.array([[6, 3, 2, 1], [8, 4, 9, 0]])
print(np4)
print(np.sort(np4))
