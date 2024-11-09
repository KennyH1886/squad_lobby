import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

We'll apply a basic machine learning model (linear regression) to predict one of the expenses (in this example, "Rent") based on the other features.
""")

# Display the data
st.write("### Monthly Budget Data")
st.dataframe(df)

# Machine Learning Code
st.write("### Machine Learning Code")
code = '''
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Select features and target variable
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
mse
'''
st.code(code, language='python')

# Machine Learning Execution
st.write("### Machine Learning Execution and Output")

# Select features and target variable
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Display the output
st.write("#### Mean Squared Error of the Model")
st.write(mse)

st.write("#### Predicted vs Actual Rent Values")
result_df = pd.DataFrame({"Actual Rent": y_test, "Predicted Rent": y_pred})
st.dataframe(result_df)