import pandas as pd
list = [10,12,13,4]
#series = pd.Series(list)  # indexing start from 0
index = ['A','B','C','D']
series = pd.Series(list,index) # indexing Manually
print(series)
print(series['A'])
print(series[0])

dic = {
    'name' :'suraj',
    'name1' :'suraj',
    'name2' :'suraj',
    'name3' :'suraj',
    '4' :'suraj'
}
print(pd.Series(dic))