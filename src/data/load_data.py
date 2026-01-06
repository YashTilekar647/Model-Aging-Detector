import pandas as pd

def load_dataset(path: str, target_col: str):
    df = pd.read_csv(path)

    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found")

    return df
