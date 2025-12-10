import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
covid = pd.read_csv('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PANDAS PROJECT\\Covid Data\\Covid Data Analysis.csv')

# Clean the data: drop rows with NaN values and ensure data types are correct
covid.dropna(subset=['State', 'Deaths'], inplace=True)
covid['State'] = covid['State'].astype(str)
covid['Deaths'] = covid['Deaths'].astype(float)

# Print cleaned data for verification
print(covid)

# Plot the bar chart
plt.bar(covid['State'].head(5), covid['Deaths'].sort_values(ascending=False).head(5))
plt.title('Covid Data')
plt.xlabel('State')
plt.ylabel('Deaths')
plt.show()
