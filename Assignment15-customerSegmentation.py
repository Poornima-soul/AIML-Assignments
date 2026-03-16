import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample mall dataset
data = {
    "Age": [19, 21, 20, 23, 31, 35, 40, 45],
    "Annual_Income": [15, 16, 17, 18, 60, 65, 70, 72],
    "Spending_Score": [39, 81, 6, 77, 40, 42, 50, 55]
}

df = pd.DataFrame(data)

# Select features
X = df[["Annual_Income", "Spending_Score"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

print(df)

# Plot clusters
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()