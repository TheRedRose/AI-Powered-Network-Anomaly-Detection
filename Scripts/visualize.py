import pandas as pd
import matplotlib.pyplot as plt
import os

# Load clustered data
df = pd.read_csv(os.path.join("data", "clustered_data.csv"))

# Plot Clusters
plt.scatter(df["feature1"], df["feature2"], c=df["cluster"], cmap="viridis")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Anomaly Detection Clustering")
plt.show()

