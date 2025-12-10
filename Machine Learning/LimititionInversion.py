import numpy as np
x = np.array([[1,2],[2,4]])   # the one coloun to dependent on another column means the first column to double of second column 
# print(np.linalg.inv(x))
y = np.array([[1,2],[1,2]])    # matrix can't be singular means one colum is not equal to another column
# print(np.linalg.inv(y))

z = np.array([[1,2,3],[1,2,5]])   # matrix row and colum must be same means only square matrix have inverse
# print(np.linalg.inv(z))