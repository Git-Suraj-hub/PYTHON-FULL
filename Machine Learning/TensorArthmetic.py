print("arthmetic using Numpy")
import numpy as np
x = np.array([[25,2,3],[20,4,6]])
print(f"{x+2}\n")
print(f"{x-2}\n")
print(f"{x*2}\n")
print(f"{x/2}\n")
print(f"{x*2+2}\n")
print(f"{x/2+2}\n")
print(np.add(x,2))

print("arthmetic using Torch\n")
import torch as t
x = t.tensor([[25,2,3],[20,4,6]])
print(f"{x+2}\n")
print(f"{x-2}\n")
print(f"{x*2}\n")
print(f"{x/2}\n")
# print(f"{x*2+2}\n")     # python operator are overloaded than we use alternative t.add and t.mul etc....
# print(f"{x/2+2}\n")
print(t.add(t.mul(x,2),2))
print(f"{t.add(t.div(x,2),2)}\n")


print("arthmetic using Tensorflow\n")

import tensorflow as tf
x = tf.Variable([[25,2,3],[20,4,6]])
print(f"{x+2}\n")
print(tf.add(x,2))
print(f"{x-2}\n")
print(f"{x*2}\n")
print(f"{x/2}\n")
# print(f"{x*2+2}\n")     # python operator are overloaded than we use alternative t.add and t.mul etc....
# print(f"{x/2+2}\n")
print(tf.add(tf.multiply(x,2),2))
print(tf.add(tf.divide(x,2),2))