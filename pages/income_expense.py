import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Sample data - simulating an income and expense dataset
data = {
    "Category": ["Rent", "Groceries", "Books", "Tuition", "Entertainment", "Transportation", "Miscellaneous", "Work-Study Income"],
    "Amount": [-400, -150, -50, -2000, -100, -75, -120, 700]  
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Conditional formatting
df["Color"] = df["Amount"].apply(lambda x: "green" if x > 0 else "red")

# Display DataFrame
st.write("Income and Expense Table:")
st.write(df[["Category", "Amount"]])

# Pie chart for expenses
expense_data = df[df["Amount"] < 0].copy()
expense_data["Amount"] = expense_data["Amount"].abs()  # Convert to positive for pie chart

# Plotting the pie chart for expenses
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(expense_data["Amount"], labels=expense_data["Category"], autopct="%1.1f%%", startangle=140)
ax.set_title("Expense Breakdown")
st.pyplot(fig)

# Calculating and displaying summary insights
total_income = df[df["Amount"] > 0]["Amount"].sum()
total_expenses = -df[df["Amount"] < 0]["Amount"].sum()  # Make expenses positive for display

st.write("\nSummary Insights:")
st.write(f"Total Income: ${total_income:,.2f}")
st.write(f"Total Expenses: ${total_expenses:,.2f}")
