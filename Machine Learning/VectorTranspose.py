import numpy as np
# 1 dimension array 
x = np.array([1,2,3,4])
print("**************** x ******************")
print(x.shape)
print(x)
print(len(x))
print(type(x))
print(x[0])
print(type(x[0]))
print("**************** y ******************")
y = x.T    # this is 1dimensional array then its not transpose because transpose need 2c and more
print(x.shape)
print(y)
print(len(y))
print(type(y))
print(y[0])
print(type(y[0]))

# 2d array and Vector

x = np.array([[1,2,3,4]])
print("**************** x ******************")
print(x.shape)
print(x)
print(len(x))
print(type(x))
print(x[0][0])
print(type(x[0][0]))
print("**************** y ******************")
y = x.T    # this is 1dimensional array then its not transpose because transpose need 2c and more
print(x.shape)
print(y)
print(len(y))
print(type(y))
print(y[0][0])
print(type(y[0][0]))