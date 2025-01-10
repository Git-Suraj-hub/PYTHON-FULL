import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1],[2],[3]])
x1 = np.dot(x,y)
print(x1)
 
import torch 
x = torch.tensor([[1,2,3],[4,5,6]])
y = torch.tensor([[1],[2],[3]])
print(torch.matmul(x,y))

import tensorflow as tf
x = tf.Variable([[1,2,3],[4,5,6]])
y = tf.Variable([[1],[2],[3]])
print(tf.matmul(x,y))
