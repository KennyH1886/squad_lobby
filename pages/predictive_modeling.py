import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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

st.title("Predictive Analysis on Monthly Budget Data")

st.write("""
### Overview
Predictive analysis is a statistical technique that uses historical data to make predictions about future outcomes. In this application, we’ll use predictive modeling to forecast one of the budget expenses (in this example, "Rent") based on other monthly budget categories. This can be useful for students to anticipate future expenses and plan accordingly.
""")

st.write("### Monthly Budget Data")
st.write("Here’s the dataset we’ll use for our analysis. Each column represents a category of expenses over a 12-month period.")
st.dataframe(df)

# Feature engineering: shift rent to create a "previous rent" column for time-series forecasting
df['Previous_Rent'] = df['Rent'].shift(1)
df = df.dropna()  # Drop rows with missing values due to shifting

st.write("""
### Step 1: Data Preparation
To prepare the data for predictive modeling, we add a new feature 'Previous Rent' which represents the rent value from the previous month. This will help in capturing any potential trend in rent across months.
""")

# Select features including previous rent as a predictor for future rent
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

st.write(f"**Training Set Size**: {X_train.shape[0]} samples")
st.write(f"**Testing Set Size**: {X_test.shape[0]} samples")

st.write("""
### Step 3: Model Selection and Training
We use a **Random Forest Regressor** for this predictive task. Random forests are a more advanced model choice, capturing complex relationships within data by averaging predictions across many decision trees.
""")

# Train Random Forest model for time-series predictive analysis
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

st.write("""
### Step 4: Making Predictions
Once the model is trained, we can use it to make predictions on the testing set. This will help us understand the accuracy of the model in predicting rent values.
""")

# Make predictions
y_pred = model.predict(X_test)

st.write("### Step 5: Model Evaluation")
st.write("""
To evaluate the performance of our model, we use:
- **Mean Squared Error (MSE)**: This metric shows the average squared difference between predicted and actual values.
- **R-Squared (R²)**: This metric indicates how well the features explain the variability of the target variable.
""")

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display evaluation metrics
st.write(f"**Mean Squared Error (MSE)**: {mse}")
st.write(f"**R-Squared (R²)**: {r2}")

st.write("""
### Step 6: Predicted vs Actual Rent Values
Below, we compare the actual "Rent" values with the predicted values from our model.
""")

# Display predicted vs actual values
result_df = pd.DataFrame({"Actual Rent": y_test, "Predicted Rent": y_pred})
st.dataframe(result_df)

st.write("""
### Step 7: Forecasting Future Rent
Using the trained model, we forecast the rent for the next month based on the latest data available.
""")

# Forecast for future months (extrapolate based on last row data)
last_row = X.iloc[[-1]]
forecast = model.predict(last_row)
st.write(f"**Forecasted Rent for Next Month**: ${forecast[0]:.2f}")

st.write("""
### Machine Learning Code
Below is the code used to perform this predictive analysis. You can use it as a template for similar predictive tasks.
""")

# Machine Learning Code Display
code = '''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Feature engineering: shift rent to create a "previous rent" column for time-series forecasting
df['Previous_Rent'] = df['Rent'].shift(1)
df = df.dropna()  # Drop rows with missing values due to shifting

# Select features including previous rent as a predictor for future rent
X = df.drop(columns=["Month", "Rent"])
y = df["Rent"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Forecast for future months
last_row = X.iloc[[-1]]
forecast = model.predict(last_row)
'''
st.code(code, language='python')

st.write("""
### Conclusion
This application demonstrated predictive analysis using a Random Forest model on monthly budget data. The addition of a previous month’s rent as a feature helps improve model accuracy, enabling better insights for future budgeting.
""")
