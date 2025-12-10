import pandas as pd
import seaborn as ss
import matplotlib.pyplot as plt
netflix = pd.read_csv('PYTHON-FULL\\PANDAS PROJECT\\Netflix\\Netflix Dataset.csv')
print(netflix)


# head() - It shows the first N rows in the data (by default, N=5).
# print(netflix.head(5))

# tail () - It shows the last N rows in the data (by default, N=5).
# print(netflix.tail(10))

# shape - It shows the total no. of rows and no. of columns of the dataframe.
# print(netflix.shape)


# size - To show No. of total values(elements) in the dataset.
# print(netflix.size)


# columns - To show each Column Name.
# print([netflix.columns])

# dtypes - To show the data-type of each column.
# print(netflix.dtypes)


# info() - To show indexes, columns, data-types of each column, memory at once.
# print(netflix.info())


# value_counts - In a column, it shows all the unique values with their count. It can be applied on a single column only.
# print(netflix.value_counts('Country'))


# unique() - It shows the all unique values of the series.
# print(netflix.Director.unique())


# nunique() - It shows the total no. of unique values in the series.
# print(netflix.nunique())


# duplicated( ) - To check row wise and detect the Duplicate rows.
# print(netflix[netflix.duplicated()])

# isnull( ) - To show where Null value is present.
# print(netflix[netflix.isnull()])

# dropna( ) - It drops the rows that contains all missing values.


# isin( ) - To show all records including particular elements.
# str.contains( ) - To get all records that contains a given string.
# str.split( ) - It splits a column's string into different columns.
# to_datetime( ) - Converts the data-type of Date-Time Column into datetime[ns] datatype.
# dt.year.value_counts( ) - It counts the occurrence of all individual years in Time column.
# groupby( ) - Groupby is used to split the data into groups based on some criteria.
# sns.countplot(df['Col_name']) - To show the count of all unique values of any column in the form of bar graph.
# max( ), min( ) - It shows the maximum/minimum value of the series.
# mean( ) - It shows the mean value of the series.

# You will learn these things also:
# Creating New Columns & Dataframe
# Filtering (Single Column & Multiple Columns)
# Filtering with And and OR
# Seaborn Library - Bar Graphs

# ..............................................

# Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
# print(netflix[netflix.duplicated()])
# print(netflix.drop_duplicates(inplace=True))
# print(netflix.shape)




# Task. 2) Is there any Null Value present in any column ? Show with Heat-map.

# ss.heatmap(netflix.isnull())
# plt.show()
# Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?
# print(netflix[netflix['Title'].isin(['House of Cards'])])


# Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.
# print(netflix.groupby('Category').Category.count())
# ss.countplot(netflix['Category'])
# plt.show()

# Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
# Q. 4) Show all the Movies that were released in year 2000.
# netflix['Release_Date'] = pd.to_datetime(netflix['Release_Date'], errors='coerce')
# netflix['Year'] = netflix['Release_Date'].dt.year
# print(netflix)
# print(netflix[netflix['Year'] == 2020.0])
# ss.countplot(netflix[netflix['Year'] == 2020.0])
# plt.show()

# Q. 5) Show only the Titles of all TV Shows that were released in India only.
# print(netflix[(netflix['Country'] == 'India') & (netflix['Category'] == 'TV Show')]['Title'] )


# Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
# print(netflix['Director'].value_counts().head(10))



# Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
# print(netflix[(netflix['Category']=='Movie')   & (netflix['Type'].str.contains('Comedy'))   | (netflix['Country'] == 'United Kingdom')      ])


# Q. 8) In how many movies/shows, Tom Cruise was cast ?
# netflix['Cast'] = netflix['Cast'].fillna('')
# print(len(netflix[netflix['Cast'].str.contains('Tom Cruise')]))

# Q. 9) What are the different Ratings defined by Netflix ?
# print(netflix['Rating'].nunique())
# print(netflix['Rating'].unique())


# # Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?
# print(netflix[(netflix['Category'] == 'Movie')    & (netflix['Rating'] == 'TV-14')      & (netflix['Country'] =='Canada')].shape)
# print(len(netflix[(netflix['Category'] == 'Movie')    & (netflix['Rating'] == 'TV-14')      & (netflix['Country'] =='Canada')]))


# Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?
# netflix['Release_Date'] = pd.to_datetime(netflix['Release_Date'], errors='coerce')
# netflix['Year'] = netflix['Release_Date'].dt.year
# print(len(netflix[(netflix['Category'] == 'TV Show') & (netflix['Rating'] =='R') & (netflix['Year'] > 2018)]))
# print(netflix[(netflix['Category'] == 'TV Show')    & (netflix['Rating'] == 'R')      & (netflix['Year'] >2018)].shape)

# Q. 10) What is the maximum duration of a Movie/Show on Netflix ?
# netflix[['Minutes','Unit']] = netflix['Duration'].str.split(' ',expand=True)
# print(netflix['Minutes'].dtypes)
# netflix['Minutes'] = pd.to_numeric(netflix['Minutes']) 
# print(netflix['Minutes'].min())
# print(netflix['Minutes'].max())
# print(netflix['Minutes'].mean())

# print(netflix['Minutes'].dtypes)


# Q. 11) Which individual country has the Highest No. of TV Shows ?
# dataTv = netflix[netflix['Category']== 'TV Show']
# print(dataTv['Country'].value_counts().head(1))

# print(dataTv['Country'].value_counts().tail(1))

# Q. 12) How can we sort the dataset by Year ?
# print(netflix.sort_values(by='Year',ascending=False))
# print(netflix.sort_values(by='Year',ascending=True))


# Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.

# print(netflix[((netflix['Category'] == 'Movie')  & (netflix['Type'] == 'Dramas') ) | ((netflix['Category'] == 'TV Show') & (netflix['Type'] == 'Kids TV') )  ]  )