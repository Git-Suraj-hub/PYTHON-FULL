print("Tensor Reduction using Numpy \n")
import numpy as np
x= np.array([[25,2,3],[20,4,6]])

print(x.sum())
print(np.sum(x))
print(x.sum(axis=0)) # sum a particular row
print(np.sum(x,0))
print(x.sum(axis=1)) # sum a particular column
print(np.sum(x,1))
print(x.mean(axis=0))   # also we find a mean , maximum value , minimum value and product of particular axis in numpy , torch and tensorflow
print("Tensor Reduction using Torch \n")
import torch
x = torch.tensor([[25,2,3],[20,4,6]])
print(torch.sum(x))
print(torch.sum(x,0)) # sum a particular row
print(x.sum(dim=0))
print(torch.sum(x,1)) # sum a particular column
print(x.sum(dim=1))

 
print("Tensor Reduction using TensorFLow \n")
import tensorflow as tf
x = tf.Variable([[25,2,3],[20,4,6]])

print(tf.reduce_sum(x))
print(tf.reduce_sum(x,0)) # sum a particular row
print(tf.reduce_sum(x,1)) # sum a particular column

