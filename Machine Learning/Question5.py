import numpy as np
x = np.array([[2],[5],[-3]])
y = np.array([[2,0,-1],[-2,3,1],[0,4,-1]])
if __name__ == "__main__":
    print(np.matmul(y,x))
