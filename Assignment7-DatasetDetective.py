import pandas as pd

# Load dataset (Example: CSV file)
df = pd.read_csv("data.csv")

# Display top 5 rows
print("Top 5 Rows:")
print(df.head())

# Find column with highest maximum value
max_values = df.max(numeric_only=True)
highest_column = max_values.idxmax()

print("\nColumn with Highest Value:", highest_column)
print("Highest Value:", max_values.max())

# Count missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
