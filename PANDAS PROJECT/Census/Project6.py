# import pandas as pd -- To import Pandas library
import pandas as pd

# pd.read_csv - To import the CSV file in Jupyter notebook
census = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\Census\Census Dataset.csv')
print(census)
# print(census[census['State_name']=='RAJASTHAN'])


# style.hide_index( ) - To hide the index of the dataframe.

# style.set_caption('Description of the dataframe') - To give a caption to the dataframe.
census.style.set_caption('This is A Dataset For india')


# isin( ) - To show all records including particular elements.


# groupby(‘Col_1’)[‘Col_2’] .sum( )[‘value’] - GroupBy – Two Keys – Apply on Col_2 grouped by Col_1.
# df[df.Col_1 == 'Element1']['Col_2'] - Filtering - Filter the records of the dataframe wrt to Element1 of Col1 and then showing results of Col2 only.
# set_index( ‘Col_Name’ ) - To set any column of a DF as an index.
# add_prefix(‘value_’) - To add prefix to the column name.
# add_suffix(‘_value’) - To add suffix to the column name.

# .......................................................................

# Q. 1) How will you hide the indexes of the dataframe.

# Q. 2) How can we set the caption / heading on the dataframe.

# Q. 3) Show the records related with the districts - New Delhi , Lucknow , Jaipur.
# print(census[census['District_name'].isin(['New Delhi','Bhilwara','Lucknow'])])

# Q. 4) Calculate state-wise :
# A. Total number of population.
# print(census.groupby('State_name').Population.sum())

# B. Total no. of the population with different religions.

# print(census.groupby('State_name')[['Hindus','Muslims','Christians','Sikhs','Buddhists']].sum())


# Q. 5) How many Male Workers were there in Maharashtra state ?
# print(census[census['State_name'] == 'MAHARASHTRA'].Male_Workers.sum())


# Q. 6) How to set a column as index of the dataframe ?
# print(census.set_index('State_name'))


# Q. 7a) Add a Suffix to the column names.
# print(census.add_suffix(' hello'))

# Q. 7b) Add a Prefix to the column names.

# print(census.add_prefix('hello ',axis=0))
