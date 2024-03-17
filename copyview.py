import numpy as np


# Copy vs. View 
np1 = np.array([0,1,2,3,4,5])


'''
# Create a View -> (connected and changes to both)
np2 = np1.view()


print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 29

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')
'''

# Create a Copy -> (not connected and does not change if one is changed)
np2 = np1.copy()


print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 29

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')

