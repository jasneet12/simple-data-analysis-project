import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("sample_data.csv")

# Show original data
print("\nOriginal Data:")
print(df)

# Clean column names (remove extra spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nAverage Salary:", df["salary"].mean())
print("Max Salary:", df["salary"].max())
print("Min Salary:", df["salary"].min())

# Salary by department
print("\nSalary by Department:")
print(df.groupby("department")["salary"].mean())

# Bar chart for salary by department
df.groupby("department")["salary"].mean().plot(kind='bar')
plt.title("Average Salary by Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("salary_by_department.png")  # Saves the chart
plt.show()

# Save summary to CSV
summary = df.groupby("department")["salary"].mean().reset_index()
summary.to_csv("department_salary_summary.csv", index=False)
print("\nSaved department salary summary.")