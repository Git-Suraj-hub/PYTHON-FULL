print("Matrix Norm Using NUMPY \n")
import numpy as np
x = np.array([[1,2,3],[2,4,6]])

Distance = (1**2 + 2**2 + 3**2 + 2**2 + 4**2 + 6**2 )**(1/2)
print(Distance)
print(np.linalg.norm(x))

print("Matrix Norm Using TORCH \n")
import torch
x= torch.tensor([[1,2,3],[2,4,6.]])
print(torch.norm(x))

print("Matrix Norm Using TENSORFLOW \n")
import tensorflow as tf
x = tf.Variable([[1,2,3],[2,4,6.]])
print(tf.norm(x))