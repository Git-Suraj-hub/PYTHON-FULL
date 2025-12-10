import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the Breast Cancer dataset
dataframe = load_diabetes()
dataset = pd.DataFrame(dataframe.data)
dataset.columns = dataframe.feature_names
X = dataset
y = dataframe['target']

# Focus on one feature (e.g., 'mean radius')
X_single_feature = X[['bmi']]  # Example: using BMI feature

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_single_feature, y, test_size=0.33, random_state=42)

# Train the Linear Regression model
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predict the target for the test set
y_pred = regression.predict(X_test)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"The Mean Square Error Of Your Model Is : {mse}")

# Plotting for one feature
plt.scatter(X_test, y_test, c='red', marker='*', label='Actual Values')  # Actual test points
plt.scatter(X_test, y_pred, c='blue', marker='o', label='Predicted Values')  # Predicted test points
plt.plot(X_test, y_pred, color='black', label='Regression Line')  # Regression Line
plt.title("Regression: Mean Radius vs Target")
plt.xlabel("Mean Radius")
plt.ylabel("Target")
plt.legend()
plt.show()

