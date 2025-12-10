import pandas as pd

wheather = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\Weather\Wheather.csv')

print(wheather)

# print(wheather.head(10))                      # head() - It shows the first N rows in the data (by default, N=5).
# print(wheather.index)                      # index - This attribute provides the index of the dataframe
# print(wheather.columns)                        # columns - It shows the name of each column
# print(wheather.dtypes)                          # dtypes - It shows the data-type of each column
# print(wheather['Weather'].unique)               # unique() - In a column, it shows all the unique values. It can be applied on a single column only, not on the whole dataframe.
# print(wheather['Weather'].nunique)              # nunique() - It shows the total no. of unique values in each column. It can be applied on a single column as well as on the whole dataframe.
# print(wheather.nunique)
# print(wheather['Weather'].count)               # count - It shows the total no. of non-null values in each column. It can be applied on a single column as well as on the whole dataframe.
# print(wheather['Weather'].value_counts())      # value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# print(wheather.info())                         # info() - Provides basic information about the dataframe.
     
# print(wheather['Weather'].info())

# Q. 1)  Find all the unique 'Wind Speed' values in the data.

# print(wheather['Wind Speed_km/h'].unique())
# print(wheather['Wind Speed_km/h'].nunique())
# print(wheather.nunique())


# Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# print(wheather[wheather.Weather == 'Clear'])
# print(wheather.groupby('Weather').get_group('Clear')) 


# Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# print(wheather[wheather['Wind Speed_km/h'] == 4])

# Q. 4) Find out all the Null Values in the data.

# print(wheather.isnull().sum())
# print(wheather.notnull().sum())



# Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# print(wheather.rename(columns={'Weather' : 'Weather Condition'} ,inplace=True ))



# Q. 6) What is the mean 'Visibility' ?

# print(wheather['Visibility_km'].mean())


# Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# print(wheather.Press_kPa.std())



# Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# print(wheather['Rel Hum_%'].var())



# Q. 9) Find all instances when 'Snow' was recorded.

# print(wheather['Weather'].value_counts())
# print(wheather[wheather['Weather'] == 'Snow'])
# print(wheather[wheather['Weather'].str.contains('Snow')])



# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# print(wheather[(wheather['Wind Speed_km/h'] > 24)  &  (wheather['Visibility_km'] ==25)] )



# Q. 11) What is the Mean value of each column against each 'Weather Condition ?
# print(wheather.iloc[:,1:].groupby('Weather').mean())



# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?
# print(wheather.iloc[:,1:].groupby('Weather').min())
# print(wheather.iloc[:,1:].groupby('Weather').max())



# Q. 13) Show all the Records where Weather Condition is Fog.

# print(wheather[wheather['Weather'] == 'Fog'])



# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# print(wheather[(wheather['Visibility_km'] > 40) & (wheather['Weather'] == 'Clear')])


# Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'

# print(wheather[(wheather['Weather']=='Clear') & (wheather['Rel Hum_%']>50)])

# or


# B. 'Visibility is above 40'

# print(wheather[wheather['Visibility_km']>40])