import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample mall dataset
data = {
    "Income": [15, 16, 17, 18, 60, 62, 65, 70],
    "Spending": [39, 81, 6, 77, 40, 42, 50, 55]
}

df = pd.DataFrame(data)

# Apply K-Means
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

print(df)

# Plot
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()