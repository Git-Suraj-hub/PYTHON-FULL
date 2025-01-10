import numpy as np
x = np.array([[1,2,3],[2,7,8],[3,8,9]])   # this is symetric matrix 
y = x.T
print(y==x)

x = np.array([[1,0,0],[0,1,0],[0,0,1]])  # this is identiy matrix
y = np.array([1,2,3])
print(np.dot(x,y))