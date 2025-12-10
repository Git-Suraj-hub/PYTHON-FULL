import pandas as pd
car = pd.read_csv('PYTHON-FULL\PANDAS PROJECT\Car Dataset\car.csv')
print(car)


# print(car.head(5))     # head() - It shows the first N rows in the data (by default, N=5)
# print(car.shape)        # shape - It shows the total no. of rows and no. of columns of the dataframe
# print(car.isnull().sum())         # df.isnull( ).sum( ) - It detects the missing values from each column of the dataframe.
# print(car.fillna('nothing'))     # fillna() - To fill the null values of a column with some particular value
# print(car.value_counts('Make'))            # value_counts - In a column, it shows all the unique values with their count. It can be applied to a single column only.
 # isin() - To show all records including particular elements
# apply() - To apply a function along any axis of DF

# ------------------------------------------------------

# Q. 1) Instruction ( For Data Cleaning ) - Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.

# Q. 2) Question ( Based on Value Counts )- Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data ?

# print(car['Make'].value_counts())


# Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.

# print(car[(car['Origin'] == 'Asia')  | (car['Origin'] == 'Europe')])
# print(car[car['Origin'].isin(['Asia','Europe'])])

# Q. 4) Instruction ( Removing unwanted records ) - Remove all the records (rows) where Weight is above 4000.

# print(car[~(car['Weight'] > 4000)])


# Q. 5) Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.

print(car['MPG_City'].apply(lambda x: x+3))