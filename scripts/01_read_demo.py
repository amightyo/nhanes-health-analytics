import pandas as pd
from pathlib import Path

DATA_RAW = Path("data/raw")

# Load Demographics data
path_demo = DATA_RAW / "P_DEMO.XPT"
df_demo = pd.read_sas(path_demo, format="xport")

print("Rows, columns:", df_demo.shape)

# Display key survey design + weight variables
cols = ["SEQN", "SDMVPSU", "SDMVSTRA"]
weight_cols = [c for c in df_demo.columns if "WGT" in c.upper() or "WT" in c.upper()]

print(df_demo[cols + weight_cols[:3]].head())  # show first 3 weight vars
