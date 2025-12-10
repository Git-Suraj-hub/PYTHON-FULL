import tensorflow as tf
x = tf.constant([[25,2,3,4],[20,4,6,10],[25,2,3,10]])
print(x)
print(x.shape)
print(len(x))
print(x[0][0])
print(x[:,1])
print(x[2,:])
print(type(x))
