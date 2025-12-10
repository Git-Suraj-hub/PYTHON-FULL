import numpy as np
zero = np.zeros(3)   # 1d array

print(zero)
print(zero.shape)
print(len(zero))
print(type(zero))
print(zero.T)

zero = np.zeros([4,3]) # 2d Vector

print(zero)
print(zero.shape)
print(len(zero))
print(type(zero))
print(zero.T)
print(len(zero.T))