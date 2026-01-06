import os
from generate_data import generate_data

# Get project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

baseline = generate_data(1000, shift=False)
current = generate_data(1000, shift=True)

baseline.to_csv(os.path.join(RAW_DATA_DIR, "baseline.csv"), index=False)
current.to_csv(os.path.join(RAW_DATA_DIR, "current.csv"), index=False)

print("Datasets created successfully in data/raw/")
