print("DOT Product Using Numpy\n")
import numpy as np
x = np.array([25,2,30])
y = np.array([0,2,10])
print(np.dot(x,y))

print("DOT Product Using Torch\n")
import torch
x= torch.tensor([25,2,30])
y = torch.tensor([0,2,10])
print(torch.dot(x,y))

print("DOT Product Using TensorFlow\n")
import tensorflow as tf
x = tf.Variable([25,2,30])
y = tf.Variable([0,2,10])

print(tf.reduce_sum(tf.multiply(x,y)))