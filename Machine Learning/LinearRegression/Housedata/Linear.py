import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset (Ensure correct file path)
dataframe = pd.read_csv('LinearRegression\\house_100_rows.csv')  # Adjust path if needed
print(dataframe.head(10))  # Display first few rows

# Extract features and target
X = dataframe[['Area']]
y = dataframe['Price']  # Use Series instead of DataFrame

import numpy as np
dataframe['Price'] += np.random.randint(-50, 50, size=len(dataframe))  # Add small noise
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
regression = LinearRegression()
regression.fit(X_train, y_train)
ypred = regression.predict(X_test)
print(regression.predict([[10000000000000]]))

# Calculate MSE
mse = mean_squared_error(y_test,ypred)
print(mse)



# Plotting
plt.scatter(X_train, y_train, color='red', marker='*', label="Training Data")
plt.scatter(X_test, y_test, color='blue', marker='o', label="Testing Data")
plt.plot(X_train, regression.predict(X_train), color='black', label="Regression Line")  # Fix

plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.show()
