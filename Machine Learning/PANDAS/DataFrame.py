import pandas as pd
import numpy.random as npr

data = npr.rand(4,3)
row = ['A','B','C','D']
col = ['Monday','Tuesday','Friday']

print(pd.DataFrame(data,index=row,columns=col))