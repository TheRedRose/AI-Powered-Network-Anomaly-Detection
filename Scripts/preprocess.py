import pandas as pd
import os
import ipaddress
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv(os.path.join("data", "network_data.csv"), encoding="ISO-8859-1")

# Convert IPs to numeric
def ip_to_int(ip):
    try:
        return int(ipaddress.IPv4Address(ip))
    except ValueError:
        return 0

if "ip.src" in df.columns and "ip.dst" in df.columns:
    df["ip.src"] = df["ip.src"].apply(ip_to_int)
    df["ip.dst"] = df["ip.dst"].apply(ip_to_int)

# Convert protocol to numeric if exists
if "protocol" in df.columns:
    df["protocol"] = df["protocol"].astype("category").cat.codes

# Drop any non-numeric columns
df = df.select_dtypes(include=["number"])

# Scale data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Convert back to DataFrame
df = pd.DataFrame(df_scaled, columns=df.columns)

# Save processed data & scaler
df.to_csv(os.path.join("data", "processed_data.csv"), index=False)
joblib.dump(scaler, os.path.join("models", "scaler.pkl"))

print("✅ Data preprocessing complete! Saved processed data.")