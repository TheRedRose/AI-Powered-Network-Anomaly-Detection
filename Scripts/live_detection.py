import sys
import os
import pandas as pd
import joblib
from scapy.all import sniff, IP

# ✅ Dynamically load the feature_extraction module
import importlib.util

spec = importlib.util.spec_from_file_location("feature_extraction", "utils/feature_extraction.py")
feature_extraction = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feature_extraction)

# Load trained model and scaler
kmeans = joblib.load(os.path.join("models", "kmeans_model.pkl"))
scaler = joblib.load(os.path.join("models", "scaler.pkl"))

def process_packet(packet):
    """
    Extracts features from a live packet, preprocesses them, and predicts anomalies.
    """
    if IP in packet:
        # ✅ Extract features using dynamically loaded module
        features = feature_extraction.extract_features(packet)

        # ✅ Convert to DataFrame
        feature_names = ["No.", "Source Port", "Destination Port", "Length", "Time"]  # Exact names
        features_df = pd.DataFrame([features], columns=feature_names)

        # ✅ Handle missing values
        features_df.fillna(0, inplace=True)

        # ✅ Scale features
        scaled_features = scaler.transform(features_df)

        # ✅ Predict cluster
        cluster = kmeans.predict(scaled_features)

        # ✅ Print the detected cluster
        print(f"📡 Packet processed -> Predicted Cluster: {cluster[0]}")

# ✅ Start live packet capture
print("🔍 Listening for network traffic...")
sniff(prn=process_packet, store=False)
