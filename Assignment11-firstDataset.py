import pandas as pd

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Identify features and labels
X = df[["Study_Hours"]]   # Feature
y = df["Marks"]           # Label

print("\nFeature (Input):")
print(X)

print("\nLabel (Output):")
print(y)

# Simple prediction example
hours = int(input("\nEnter study hours to predict marks: "))
predicted_marks = hours * 10 + 30

print("Predicted Marks:", predicted_marks)