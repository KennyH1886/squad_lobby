import streamlit as st
import pandas as pd

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
st.title("Monthly Budget Overview")

# Display the data as a table
st.dataframe(df)