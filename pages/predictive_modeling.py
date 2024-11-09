import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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
st.title("Predictive Analysis on Monthly Budget Data")

st.write("""
### Overview
Predictive analysis is a statistical technique that uses historical data to make predictions about future outcomes. In this application, we’ll use predictive modeling to forecast one of the budget expenses (in this example, "Rent") based on other monthly budget categories. This can be useful for students to anticipate future expenses and plan accordingly.
""")

st.write("### Monthly Budget Data")
st.write("Here’s the dataset we’ll use for our analysis. Each column represents a category of expenses over a 12-month period.")
st.dataframe(df)

st.write("""
### Step 1: Data Preparation
To prepare the data for predictive modeling, we need to:
- **Select a Target Variable**: In this example, we’ll use "Rent" as the target we want to predict.
- **Select Features**: We’ll use other categories such as "Groceries", "Books", "Entertainment", etc., as features that may help predict rent.
- **Split the Data**: We’ll divide the data into training and testing sets to evaluate the model’s accuracy.
""")

# Select features and target variable
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

st.write("### Step 2: Splitting the Data")
st.write("""
We split the data into training and testing sets. The training set will be used to train the model, while the testing set will evaluate its accuracy.
""")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

st.write(f"**Training Set Size**: {X_train.shape[0]} samples")
st.write(f"**Testing Set Size**: {X_test.shape[0]} samples")

st.write("""
### Step 3: Model Selection and Training
We use a simple **Linear Regression** model for this predictive task. Linear regression is a straightforward and commonly used method for predicting a continuous target variable by finding the linear relationship between the target and the features.
""")

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

st.write("""
### Step 4: Making Predictions
Once the model is trained, we can use it to make predictions on the testing set. These predictions will give us an idea of how well the model has learned the patterns in the data.
""")

# Make predictions
y_pred = model.predict(X_test)

st.write("### Step 5: Model Evaluation")
st.write("""
To evaluate the performance of our model, we use two metrics:
- **Mean Squared Error (MSE)**: This metric shows the average squared difference between predicted and actual values. A lower MSE indicates better performance.
- **R-Squared (R²)**: This metric indicates how well the features explain the variability of the target variable. An R² close to 1 implies a good fit.
""")

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display evaluation metrics
st.write(f"**Mean Squared Error (MSE)**: {mse}")
st.write(f"**R-Squared (R²)**: {r2}")

st.write("""
### Step 6: Predicted vs Actual Rent Values
Here we compare the actual "Rent" values with the predicted values from our model. This comparison helps us visualize the model’s accuracy.
""")

# Display predicted vs actual values
result_df = pd.DataFrame({"Actual Rent": y_test, "Predicted Rent": y_pred})
st.dataframe(result_df)

st.write("""
### Machine Learning Code
Below is the code used to perform this predictive analysis. You can use it as a template for similar predictive tasks.
""")

# Machine Learning Code Display
code = '''
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display predicted vs actual values
result_df = pd.DataFrame({"Actual Rent": y_test, "Predicted Rent": y_pred})
'''
st.code(code, language='python')

st.write("""
### Conclusion
This application demonstrated a basic predictive analysis using a linear regression model on monthly budget data. While this model is relatively simple, more advanced techniques and larger datasets can yield even more accurate predictions.

Predictive modeling can provide valuable insights, helping students anticipate future expenses and make informed budgeting decisions.
""")