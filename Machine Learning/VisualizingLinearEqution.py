import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,10000)

# y1= 4*x + 1
# y2 = 2 + 4*x   # No solution 
y1 = 3*x
y2 = 1+(5*x) / 2
ax  = plt.subplot()
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(0,3)
ax.set_ylim(0,10)
ax.plot(x,y1)
ax.plot(x,y2)
plt.axvline(x=2,color="purple",linestyle = '--')
plt.axhline(y=6,color="purple",linestyle = '--')
plt.show()