import joblib
import pandas as pd
import os
import chardet  # Auto-detect encoding

# Detect encoding of the file
def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read(100000))  # Read first 100KB
    return result['encoding']

# Load the dataset with correct encoding
file_path = os.path.join("data", "processed_data.csv")  # or network_data.csv
encoding = detect_encoding(file_path)
df_new = pd.read_csv(file_path, encoding=encoding)

# Handle NaN values
df_new.fillna(df_new.mean(), inplace=True)  # Fill NaN with column means

# Load trained model and scaler
kmeans = joblib.load(os.path.join("models", "kmeans_model.pkl"))
scaler = joblib.load(os.path.join("models", "scaler.pkl"))

# Scale data
df_scaled = scaler.transform(df_new.select_dtypes(include=['float64', 'int64']))  # Ensure only numerical columns

# Predict anomalies
df_new["cluster"] = kmeans.predict(df_scaled)

# Print anomalies (adjust threshold if needed)
anomalies = df_new[df_new["cluster"] == -1]  # If -1 represents anomalies in your model
print("⚠ Detected anomalies:", anomalies)
