print("hadamard Multiply Using Numpy ")
import numpy as np
x = np.array([[20,2,3],[25,2,5]])
y = x+2

print(x*y)
print(np.multiply(x,y))

print("hadamard Multiply Using Torch \n ")
import torch as t
x = t.tensor([[20,2,3],[25,2,5]])
y = x+2

print(x*y)
print(t.multiply(x,y))

print("hadamard Multiply Using Tensorflow \n ")
import tensorflow as tf
x = tf.Variable([[20,2,3],[25,2,5]])
y = x+2

print(x*y)
print(tf.multiply(x,y))