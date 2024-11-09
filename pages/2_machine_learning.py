import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Rent": [397, 585, 396, 404, 346, 570, 476, 483, 436, 395, 515, 338],
    "Groceries": [129, 164, 103, 157, 82, 156, 64, 77, 151, 90, 98, 152],
    "Books": [32, 97, 99, 22, 48, 114, 104, 2, 48, 60, 16, 95],
    "Tuition": [3233, 0, 0, 0, 0, 0, 4833, 0, 0, 0, 0, 0],
    "Entertainment": [31, 43, 73, 91, 8, 82, 54, 73, 66, 60, 91, 30],
    "Transportation": [65, 67, 54, 72, 41, 79, 48, 38, 64, 95, 97, 53],
    "Miscellaneous": [234, 164, 198, 106, 74, 141, 267, 216, 261, 92, 275, 120],
    "Work-Study Deposits": [737, 943, 701, 722, 500, 606, 897, 669, 512, 952, 932, 967]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Monthly Budget Data Analysis with Machine Learning")

# Explanation of the data
st.write("""
### Data Overview
This dataset represents a student's monthly budget, with categories including Rent, Groceries, Books, Tuition, Entertainment, Transportation, Miscellaneous, and Work-Study Deposits.

We'll apply machine learning models (Linear Regression and Random Forest) to predict one of the expenses (in this example, "Rent") based on the other features.
""")

# Display the data
st.write("### Monthly Budget Data")
st.dataframe(df)

# Machine Learning Execution
st.write("### Machine Learning Execution and Output")

# Select features and target variable
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train and evaluate Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
mse_linear = mean_squared_error(y_test, y_pred_linear)

# Train and evaluate Random Forest Regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=0)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)


# Display predicted vs actual values for Random Forest model
result_df = pd.DataFrame({"Actual Rent": y_test,  "Predicted Rent (Random Forest)": y_pred_rf})
st.write("#### Predicted vs Actual Rent Values")
st.dataframe(result_df)

# Plotting the actual vs predicted rent values
st.write("### Predicted vs Actual Rent Values Visualization")

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual Rent', marker='o', linestyle='-', color='blue')
plt.plot(y_pred_rf, label='Predicted Rent (Random Forest)', marker='s', linestyle=':', color='red')
plt.xlabel("Data Point Index")
plt.ylabel("Rent")
plt.title("Actual vs Predicted Rent Values")
plt.legend()
st.pyplot(plt)
