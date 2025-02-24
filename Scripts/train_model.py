import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# Load Preprocessed Data
df = pd.read_csv(os.path.join("data", "processed_data.csv"))

# Drop any NaN values
df = df.dropna()

# Select relevant features
selected_features = ["feature1", "feature2", "feature3", "feature4", "feature5"]
df = df[selected_features]

# Train K-Means Model
kmeans = KMeans(n_clusters=2, random_state=42)
df["cluster"] = kmeans.fit_predict(df)

# Save Model
joblib.dump(kmeans, os.path.join("models", "kmeans_model.pkl"))

# Save clustered data
df.to_csv(os.path.join("data", "clustered_data.csv"), index=False)

print("Model Trained and Saved $")