# import pandas as pd -- To import Pandas library
import pandas as pd

# pd.read_csv - To import the CSV file in Jupyter notebook
Police = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\Police\Police DataSet.csv')
print(Police)

# head() - It shows the first N rows in the data (by default, N=5)
# print(Police.head(10))

# df.isnull( ).sum( ) - It detects the missing values from each column of the dataframe.
# print(Police.isnull())
# # print(Police.isnull().sum())


# df.drop(‘Col_name’ )   - To drop a column from dataframe.
# print(Police.drop(columns='country_name'))

# value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# print(Police.value_counts('driver_gender'))
# print(Police.count())


# df.groupby(‘Col_1’)[‘Col_2’] .sum( ) - To create groups - Two Keys – Apply on Col_2 grouped by Col_1.
# print(Police.groupby('driver_gender')['driver_age'].apply(lambda x: ', '.join(x.astype(str))))

# df['Column_name'].map( { old1:new1 , old2:new2} ) – Change the all values of a column from old to new. We have to write for all values of column otherwise Nan will appear.
# df['Column_name'].mean() - To show Mean value of a column.
# df.groupby('Column_1').Column_2.describe() - To create groups based on Column1 and show statistics summary based on Column2.

# .......................................................................

# Q. 1) Instruction ( For Data Cleaning ) - Remove the column that only contains missing values.
# print(Police.drop(columns='country_name' , inplace=True))
# print(Police)

# Q. 2) Question ( Based on Filtering + Value Counts ) - For Speeding , were Men or Women stopped more often ? 
# print(Police.driver_gender.value_counts())
# print(Police[Police.violation == 'Speeding' ].value_counts('driver_gender'))

# Q. 3) Question ( Groupby ) - Does gender affect who gets searched during a stop ?
# print(Police.groupby('driver_gender')['search_conducted'].sum())


# Question ( mapping + data-type casting )
# Q. 4) Question ( mapping + data-type casting ) - What is the mean stop_duration ?
# print(Police.stop_duration.value_counts())
# Police['stop_duration'] = Police['stop_duration'].map({'0-15 Min' :7.5, '16-30 Min':24 ,'30+ Min':45})
# print(Police)
# print(Police.stop_duration.mean())

# Q. 5) Question ( Groupby , Describe ) - Compare the age distributions for each violation.
# print(Police.groupby('violation').driver_age.describe())