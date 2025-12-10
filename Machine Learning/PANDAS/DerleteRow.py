import pandas as pd
csv = pd.read_csv('PYTHON-FULL\\Machine Learning\\PANDAS\\Book1.csv')
# csv.drop("Unnamed: 9",axis=1,inplace=True)
csv.drop(3,inplace=True)
print(csv)