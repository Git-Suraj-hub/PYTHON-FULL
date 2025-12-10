# import pandas as pd -- To import Pandas library
import pandas as pd


# pd.read_csv - To import the CSV file in Jupyter notebook
house = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\House Analysis\London House Analysis.csv')
print(house)


# df.count() - It counts the no. of non-null values of each column.
# print(house.count())

# df.isnull().sum() - It detects the missing values from the dataframe.
# print(house.isnull().sum())


# import seaborn as sns - To import the Seaborn library.
import seaborn as sns
# import matplotlib.pyplot as plt - To import the Matplotlib library.
import matplotlib.pyplot as plt
# sns.heatmap(df.isnull()) - It will show the all columns & missing values in them in heat map form.

# sns.heatmap(house.isnull())

# plt.show() - To show the plot.
# plt.show()


# df.dtypes - To show the datatype of each column.
# print(house.dtypes)

# pd.to_datetime(df.Date_Time_Col) - Converts the data-type of Date-Time Column into datetime[ns] datatype.

# df.Time_Col.dt.year - Creating a new column with only year values

# df.Time_Col.dt.month - Creating a new column with only month values.
# df.insert( index , ‘new_column_name’, new_column_values) - To insert a New column at a particular position with values in it.
# df.drop(['Col_name'] , axis=1 , inplace = True) - To drop a column from the dataframe permanently.
# df.groupby(‘Col_name’) - To form groups of all unique values of the column.
# df[df.Col_1 = = ‘Element1’] - Filtering – We are accessing all records with Element1 only of Col_1.
# df.groupby(‘Col_1’)[‘Col_2’] .mean( ) - To create groups - Two Keys – Apply on Col_2 grouped by Col_1.

# -----------------------------------------------------

# Q. 1) Convert the Datatype of 'Date' column to Date-Time format.
house.date = pd.to_datetime(house.date)


# Q. 2) Add a new column ''year'' in the dataframe, which contains years only.
house['Year'] = house['date'].dt.year
print(house)

# (2.B) Add a new column ''month'' as 2nd column in the dataframe, which contains month only.
house.insert(2,'Month',house.date.dt.month)
print(house)


# Q. 3) Remove the columns 'year' and 'month' from the dataframe.
# house.drop(['Month','Year'] ,axis=1, inplace=True)
# print(house)

# Q. 4) Show all the records where 'No. of Crimes' is 0. And, how many such records are there ?
# print(house[house['no_of_crimes'] == 0])
# print(len(house[house['no_of_crimes'] == 0]))

# Q. 5) What is the maximum & minimum 'average_price' per year in england ?
# df1 = house[house['area'] == 'england']
# print(df1.average_price.min())
# print(df1.average_price.max())

# Q. 6) What is the Maximum & Minimum No. of Crimes recorded per area ?

# print(house.groupby('area').no_of_crimes.max())
# print(house.groupby('area').no_of_crimes.min())

# Q. 7) Show the total count of records of each area, where average price is less than 100000.
print(house[house['average_price']>100000].area.value_counts())