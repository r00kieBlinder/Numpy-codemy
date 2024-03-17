import numpy as np

# Search 
np1 = np.array([1,2,3,4,5,6,7,8,9,10, 3])

x = np.where(np1 == 3)

print(np1)
print(x)  # returns a tuple 
print(x[0]) # returns the first element of the tuple
print(np1[x[0]]) # retunrs the number at those particular indices   



# Returns even items 
y = np.where(np1 % 2 == 0) 
print(np1)
print(y)
print(np1[y[0]]) # returning the elements in relation to y

# Returns odd items 
z = np.where(np1 % 2 != 0)
print(np1)
print(z)
print(np1[z[0]]) # returning the elements in relation to z 