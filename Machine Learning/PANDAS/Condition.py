import pandas as pd
csv = pd.read_csv('PYTHON-FULL\\Machine Learning\\PANDAS\Book1.csv')
print(csv)
# print(csv == 1)
# print(csv[csv == 1])
# print(csv[csv == 1][["Index","City"]])
print(csv[csv["Company"]=="Downs"])
