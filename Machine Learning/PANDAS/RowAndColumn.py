import pandas as pd
import numpy as np
csv = pd.read_csv('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\Machine Learning\PANDAS\\Book1.csv')
csv["Color"] = np.nan*len(csv)
csv["Company"] = ['Male']*len(csv)
csv.insert(2,"Married","L")
csv = csv.assign(salary=["100"]*len(csv))
print(csv)