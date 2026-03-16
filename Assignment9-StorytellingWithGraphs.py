import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [78, 85, 90, 66, 72]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(df["Marks"], labels=df["Student"], autopct='%1.1f%%')
plt.title("Marks Distribution - Pie Chart")
plt.show()

# Histogram
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()





