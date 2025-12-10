import pandas as pd
csv = pd.read_csv('PYTHON-FULL\\Machine Learning\PANDAS\\Book1.csv')
# print(csv.loc[[0,1,0]])
# print(csv.loc[0])
# print(csv.iloc[0])
# print(csv.iloc[[0,1,0]])
# print(csv.loc[0,'Customer Id'])
# print(csv.loc[[0,1],'Customer Id'])
print(csv.loc[[0,1],['Customer Id','City']])