data = {
    "Category": [
        "Rent",
        "Groceries",
        "Books and Supplies",
        "Tuition",
        "Entertainment",
        "Transportation",
        "Miscellaneous",
        "Part-Time Job Income",
        "Scholarship Income",
        "Freelance Income"
    ],
    "Amount": [
        -1200,     # Rent
        -300,      # Groceries
        -100,      # Books and Supplies
        -5000,     # Tuition
        -200,      # Entertainment
        -150,      # Transportation
        -100,      # Miscellaneous
        1200,      # Part-Time Job Income
        3000,      # Scholarship Income
        500        # Freelance Income
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Conditional formatting for income and expenses
df["Color"] = df["Amount"].apply(lambda x: "green" if x > 0 else "red")

# Display the DataFrame
st.write("Income and Expense Table for a College Student:")
st.write(df[["Category", "Amount"]])

# Pie chart for expenses only
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
st.write(f"Net Balance: ${total_income - total_expenses:,.2f}")
