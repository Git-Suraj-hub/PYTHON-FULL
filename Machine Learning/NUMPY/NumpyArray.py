# import Numpy For Create a Array In Python
import numpy as np

# Create A Array In Numpy

# x = [1,2,3,4,5]

# # y = np.array(x)
# y = np.array([1,2,3,4,5])
# print(y)
# print(type(y))

# create A Array In Numpy for User Input 

# l = []
# x = int(input("Enter A Number Of Array : "))
# for i in range(x):
#     y = int(input(f"Enter A {i+1} Array Element : "))
    
#     l.append(y)
# z = np.array(l)   
# print(z)


# check A Dimension In array 

y = np.array([1,2,3,4,5])
y1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
y2 = np.array([[[1,2,3,4],[4,5,6,7],[9,10,11,12]]])
y3 = np.array([[[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]]])
print(y)
print(f"The Dimension Of This Array Is : {y.ndim}")
print(y1)
print(f"The Dimension Of This Array Is : {y1.ndim}")
print(y2)
print(f"The Dimension Of This Array Is : {y2.ndim}")
print(y3)
print(f"The Dimension Of This Array Is : {y3.ndim}")

# create a n number of dimension

y4 = np.array([[1,2,3,4],[4,5,6,7]],ndmin=10)
print(f"The Dimension Of This Array Is : {y4.ndim}")
print(y4)

