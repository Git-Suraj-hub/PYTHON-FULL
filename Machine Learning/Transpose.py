print("Transpose Using Numpy ")
#transpose using Numpy
import numpy as np
x = np.array([[25,2,3],[20,4,6]])
print("**** the Original Matrix *******")
print(f"{x}\n")
print("******* after Transpose Matrix ****")
Transpose = x.T
print(Transpose)

print("Transpose Using Torch \n")
#transpose using Torch
import torch 
x = torch.tensor([[25,2,3],[20,4,6]])
print("**** the Original Matrix *******")
print(f"{x}\n")
Transpose = x.T
print("******* after Transpose Matrix ****")
print(Transpose)

print("Transpose Using TENSORFLOW \n")
#transpose using Tensorflow
import tensorflow as tf
x = tf.Variable([[25,2,3],[20,4,6]])
print("**** the Original Matrix *******")
print(f"{x}\n")
Transpose = tf.transpose(x)
print("******* after Transpose Matrix ****")
print(Transpose)
