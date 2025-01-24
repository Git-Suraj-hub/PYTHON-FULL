import numpy as np
from Question5 import x,y

z = np.array([[0],[-4],[6]])
a = np.concatenate((x,z) ,axis=1)
print(np.dot(y,a))