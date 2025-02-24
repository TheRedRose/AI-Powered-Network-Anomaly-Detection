import os

# Step1: Preprocess Data
os.system("python Scripts/preprocess.py")

# Step2: Train Model
os.system("python Scripts/train_model.py")

# Step3: Detect Anomalies
os.system("python Scripts/detect_anomalies.py")
