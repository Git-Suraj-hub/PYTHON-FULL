import numpy as np
x = np.array([25,2,5])

# How to Find Norms And Distance
# l2 Norms
print("****** This is L2 Norms *********")
Distance = (25**2 + 2**2+ 5**2)**(1/2)     # this is manual formula
print(f"The Distance Of Vector x is {Distance}")
D = np.linalg.norm(x)    # this is inbuilt fumction in numpy to find Distance linear algebra (linalg) module
print(f"The Distance Of Vector x is {D}\n")

#l1 Norms
print("****** This is L1 Norms *********")
Distance = np.abs(25)  + np.abs(2) + np.abs(5)    # this is manual formula
print(f"The Distance Of Vector x is {Distance}")
D = np.linalg.norm(x,1)    # this is inbuilt fumction in numpy to find Distance linear algebra (linalg) module
print(f"The Distance Of Vector x is {D}\n")


# l infinitre norms
print("****** This is L infinte Norms *********")
Distance = np.max([np.abs(25),np.abs(2),np.abs(5)])  # this is manual formula
print(f"The Distance Of Vector x is {Distance}")
D = np.linalg.norm(x,np.inf)    # this is inbuilt fumction in numpy to find Distance linear algebra (linalg) module
print(f"The Distance Of Vector x is {D}\n")

# square l2 norms
print("****** This is square  L2 Norms *********")
Distance = (25**2 + 2**2 + 5**2)  # this is manual formula
print(f"The Distance Of Vector x is {Distance}")
D = np.dot(x,x)   # this is inbuilt fumction in numpy to find Distance linear algebra (linalg) module
print(f"The Distance Of Vector x is {D}\n")


