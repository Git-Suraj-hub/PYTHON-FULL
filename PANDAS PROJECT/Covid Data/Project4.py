# import pandas as pd -- To import Pandas library
import pandas as pd

# import seaborn as sns - To import the Seaborn library.
import seaborn as sns

# import matplotlib.pyplot as plt - To import the Matplotlib library.
import matplotlib.pyplot as plt

# pd.read_csv - To import the CSV file in Jupyter notebook
covid = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\Covid Data\Covid Data Analysis.csv')
print(covid)

# df.count() - It counts the no. of non-null values of each column.
# print(covid.count())


# df.isnull().sum() - It detects the missing values from the dataframe.
# print(covid.isnull().sum())

# sns.heatmap(df.isnull()) - It will show the all columns & missing values in them in heat map form.
# sns.heatmap(covid.isnull())
# plt.show()
# plt.show() - To show the plot.
# df.groupby(‘Col_name’) - To form groups of all unique values of the column.
# df.sort_values(by= ['Col_name'] ) - Sort the entire dataframe by the values of the given column.
# print(covid.sort_values(by=['Deaths'],ascending=False))
     
# df[df.Col_1 = = ‘Element1’] - Filtering – We are accessing all records with Element1 only of Col_1.
# print(covid[covid.Region == 'Mainland China'])
# .......................................................................

# Q. 1) Show the number of Confirmed, Deaths and Recovered cases in each Region.
# print(covid.groupby('Region')[['Confirmed' ,'Deaths','Recovered']].sum().sort_values(by='Recovered',ascending=False))


# Q. 2) Remove all the records where the Confirmed Cases is Less Than 10.
# print(covid[~covid['Confirmed']<10])

# Q. 3) In which Region, maximum number of Confirmed cases were recorded ?
# print(covid.groupby('Region').Confirmed.sum().sort_values(ascending=False))


# Q. 4) In which Region, minimum number of Deaths cases were recorded ?
# print(covid.groupby('Region').Deaths.sum().sort_values(ascending=False))

# Q. 5) How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020 ?
# print(covid[(covid['Region'] == 'US') & (covid['Date'] < '2020-04-29')])


# Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order.
# print(covid.Confirmed.sort_values(ascending=True))
# print(covid.sort_values(by='Confirmed'))


# Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.
# print(covid['Recovered'].sort_values(ascending=False))
# print(covid.sort_values(by='Recovered',ascending=False))