# 4b + 2c = 4
# -5b -3c = -7
import numpy as np
x = np.array([[4,2.],[-5,-3.]])
y=np.array([4,-7.])
inv = np.linalg.inv(x)
w = np.dot(inv,y)
print(w)   # so the b value is -1 and c is 4

import torch
x1 = torch.from_numpy(x)
y1 = torch.from_numpy(y)
inv = torch.inverse(x1)
w1 = torch.matmul(inv,y1)
print(w1)

import tensorflow as tf
x2 = tf.convert_to_tensor(x)
y2 = tf.convert_to_tensor(y)
inv = tf.linalg.inv(x2)
y2 = tf.reshape(y2, (-1, 1))  # We reshape tensors in TensorFlow (or any array in general) to ensure they have the appropriate dimensions for the operations we want to perform. In your specific case, we needed to reshape the vector y to make it compatible for matrix multiplication with the matrix x.
w3 = tf.matmul(inv,y2)
w3=tf.reshape(w3,(-1))  #x has shape (2, 2)
# y initially has shape (2,)
print(w3)